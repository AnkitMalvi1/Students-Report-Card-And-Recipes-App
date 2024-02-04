from .models import Student
import time
from django.core.mail import send_mail
from django.conf import settings

def run_this_function():
    print("Function Started")
    time.sleep(1)
    print("Function Executed")


def send_email_to_client():
    subject = "Email from Django Server!"    
    message = "This is test message from django server email."

    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ankitmalviya06219@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)