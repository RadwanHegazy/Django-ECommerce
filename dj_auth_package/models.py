from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import timedelta
from .utils import send_reset_password_email
import random

User = get_user_model()

class ResetPasswordModel(models.Model) :
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4)
    user = models.ForeignKey(User, related_name='user_reset_password_form' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    otp_code = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return str(self.id)
    

@receiver(post_save, sender=ResetPasswordModel)
def update_finsihed_at_date (created, instance:ResetPasswordModel, **kwargs):
    if not created:
        return
    instance.finished_at = instance.created_at + timedelta(hours=2)
    instance.otp_code = ''.join(map(str,[random.randrange(0,9) for i in range(7)]))
    instance.save()
    