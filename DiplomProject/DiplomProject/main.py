import os
import django
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
import smtplib
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
# from icrawler.builtin import GoogleImageCrawler


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DiplomProject.settings')
django.setup()


from user.models import User
from events.models import Event
from django.utils import timezone
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)


# def create_and_upload_file(file_name='test.txt', file_content='Hey Dude!'):
#     try:
#         my_file = drive.CreateFile({'title': f'{file_name}'})
#         my_file.SetContentString(file_content)
#         my_file.Upload()
#
#         return f'File {file_name} was uploaded!Have a good day!'
#     except Exception as _ex:
#         return 'Got some trouble, check your code please!'


# def upload_dir(dir_path=''):
#     try:
#
#         for file_name in os.listdir(dir_path):
#             my_file = drive.CreateFile({'title': f'{file_name}'})
#             my_file.SetContentFile(os.path.join(dir_path, file_name))
#             my_file.Upload()
#
#             print(f'File {file_name} was uploaded!')
#
#         return 'Success!Have a good day!'
#     except Exception as _ex:
#         return 'Got some trouble, check your code please!'
#
#
# def download_dir(dir_path=''):
#     print('!!!!!!!!!!')
#     try:
#         print(drive.listdir(dir_path))
#         for file_name in drive.listdir(dir_path):
#             print(f'File {file_name} was downloaded!')
#
#         return 'Success!Have a good day!'
#     except Exception as _ex:
#         return 'Got some trouble, check your code please!'


def send_email_to_all_users():
    sender = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    # sender = 'maksimenkasp@yandex.ru'
    # password = 'yowjajfcjrcwtpvo'
    to_email = []
    message = 'TEST MAIL'
    users = User.objects.filter(events__meeting_time__lt=timezone.now().date() + timezone.timedelta(days=1))
    for user in users:
        to_email.append(user.email)
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    try:
        server.login(sender, password)
        server.sendmail(sender, to_email, message)
        server.quit()
        return 'Отправилось'
    except Exception as _ex:
        return f"{_ex}\n Проверь пароль"


def main():

    # print(create_and_upload_file(file_name='hello.txt', file_content='Hello Friend'))
    # print(upload_dir(dir_path='C:\Project\DiplomProject\events\media'))
    # print(download_dir('/'))
    print('почта до')
    print(send_email_to_all_users())
    print('почта после')


if __name__ == '__main__':
    main()
