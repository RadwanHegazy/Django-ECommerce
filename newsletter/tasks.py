from celery import shared_task
from users.models import User
from django.core.mail import send_mail
from core.settings.base import EMAIL_HOST_USER

@shared_task
def send_newsletter(title, content) : 
    users = User.objects.exclude(is_superuser=True, is_staff=True).values_list('email')
    users_emails = [i[0] for i in users]

    send_mail(
        subject=title,
        message=content,
        from_email=EMAIL_HOST_USER,
        recipient_list=users_emails
    )

