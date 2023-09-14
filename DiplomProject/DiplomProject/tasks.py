from celery import shared_task, Task
from celery import app

from my_email import send_email_to_all_users


@app.task(bind=True)
def some_func(self: Task):
    send_email_to_all_users()


# @shared_task
# def logging(*args, **kwargs):
#     with open("text.txt", "w") as f:
#         f.write(str(args) + " " + str(kwargs))
#     print(args)
#     print(kwargs)
#
#
# @shared_task
# def create_object():
#     print("*:8000")
