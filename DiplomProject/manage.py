#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from my_email import send_email_to_all_users
# from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DiplomProject.settings')

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)


def main():
    """Run administrative tasks."""
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DiplomProject.settings')
    print("Дошла")
    # send_email_to_all_users()
    print("Дошла !!!!!!!!!!")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
