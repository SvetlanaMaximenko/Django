import os

from celery import Celery

from celery import shared_task, Task
from celery import app
from django.core.mail import send_mail



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DiplomProject.settings')

app = Celery('DiplomProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()




@app.task
def some_func():
    print('Input to task')
    send_email_to_all_users()


def send_email_to_all_users():
    print("!!!!!!!!!!!1")

    # sender = settings.EMAIL_HOST_USER
    # password = settings.EMAIL_HOST_PASSWORD
    to_email = ['sv-maximenko@rambler.ru']
    # message = 'Ваше событие состоится завтра'
    # users = User.objects.filter(events__meeting_time__lt=timezone.now().date() + timezone.timedelta(days=1))
    # for user in users:
    #     to_email.append(user.email)

    send_mail(
        'Subject here',
        'Here is the message.',
        ['sv-maximenko@rambler.ru'],
        ['sv-maximenko@rambler.ru'],
        fail_silently=False,
    )
    return
    # server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    # try:
    #     print('!!!!!!!!!!!!2')
    #     server.login(sender, password)
    #     server.sendmail(sender, to_email, message)
    #     server.quit()
    #
    #     return 'Отправилось'
    # except Exception as _ex:
    #     return f"{_ex}\n Проверь пароль"
