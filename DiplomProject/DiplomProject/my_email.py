import os

import django
# import smtplib
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DiplomProject.settings')
django.setup()


from user.models import User
from events.models import Event
from django.utils import timezone


def send_email_to_all_users():
    print("!!!!!!!!!!!1")

    # sender = settings.EMAIL_HOST_USER
    # password = settings.EMAIL_HOST_PASSWORD
    to_email = ['sv-maximenko@rambler.ru']
    # message = 'Ваше событие состоится завтра'
    users = User.objects.filter(events__meeting_time__lt=timezone.now().date() + timezone.timedelta(days=1))
    for user in users:
        to_email.append(user.email)

    send_mail(
        'Subject here',
        'Here is the message.',
        ['sv-maximenko@rambler.ru'],
        ['sv-maximenko@rambler.ru'],
        fail_silently=False,
    )
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


def main():

    print(send_email_to_all_users())


if __name__ == '__main__':
    main()



