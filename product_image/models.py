from django.db import models
from cloudinary.models import CloudinaryField

class Product_Image(models.Model) : 
    image = CloudinaryField('image')

    def __str__(self):
        return self.image.url