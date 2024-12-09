from django.db import models
from category.models import Category
from product_image.models import Product_Image

class Product(models.Model) : 
    title = models.CharField(max_length=225)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=100, decimal_places=0)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    images = models.ManyToManyField(Product_Image, related_name='product_images')

    def __str__(self):
        return self.title