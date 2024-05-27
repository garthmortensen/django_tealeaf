from pathlib import Path
import os
from dotenv import load_dotenv

from django.core.mail import send_mail
from django.http import HttpResponse

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / '.env'
load_dotenv(dotenv_path)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True  # security: encrypt data from django to email
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # gmail app password. https://stackoverflow.com/a/76439245


def send_test_email(request):
    # send_mail is a Django utility to send email
    # fail_silently: boolean. If False, send_mail will raise an smtplib.SMTPException if an error occurs
    send_mail(
        subject="Test Email",
        message="This is a test email sent from Django.",
        from_email=EMAIL_HOST_USER,
        recipient_list=["mortensengarth@hotmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email sent!")  # HttpResponse sent to the client after the email is sent
