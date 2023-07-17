from celery import shared_task
from django.contrib.auth import get_user_model
from .models import Event
from django.core.mail import EmailMultiAlternatives


@shared_task(ignore_result=True)
def send_user_event(user_id: int, event: Event):
    user_model = get_user_model()

    try:
        user = user_model.objects.get(id=user_id)
    except user_model.DoesNotExist:
        return

    if not user.email:
        return

    email = EmailMultiAlternatives(
        subject=f"Уведомляем вас, что вы согласились посетить {event.name}. Мероприятие проходит завтра в {event.description} Начало в {event.meeting_time}.",
        to=[user.email],
    )

    email.send()
