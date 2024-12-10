from .models import Newsletter
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import send_newsletter

@receiver(post_save, sender=Newsletter)
def SendMessagetoUserEmail(created, instance:Newsletter, **kwargs) : 
    if not created:
        return

    # celery task for implement action in background
    send_newsletter.delay(instance.title, instance.content)

  
