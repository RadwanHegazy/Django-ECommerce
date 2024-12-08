from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

class LoginByChoices(models.Choices) :
    email = 'email'
    facebook = "facebook"
    google = "google"

class User (AbstractUser) : 
    objects = CustomUserManager()

    groups = None
    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True)
    phone = PhoneNumberField(null=True, blank=True)
    full_name = models.CharField(max_length=225)
    picture = CloudinaryField("image",folder='user-pics/', null=True, blank=True)
    password = models.TextField(null=True, blank=True)

    REQUIRED_FIELDS = ['full_name','phone']
    USERNAME_FIELD = 'email'

    login_by = models.CharField(max_length=10, choices=LoginByChoices, default=LoginByChoices.email)

    def __str__(self):
        return self.full_name
    