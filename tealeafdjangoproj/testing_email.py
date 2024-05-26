from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    # send_mail is a Django utility to send email
    # fail_silently: boolean. If False, send_mail will raise an smtplib.SMTPException if an error occurs
    send_mail(
        subject="Test Email",
        message="This is a test email sent from Django.",
        from_email="your-email@example.com",
        recipient_list=["hi@hotmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email sent!")  # HttpResponse sent to the client after the email is sent
