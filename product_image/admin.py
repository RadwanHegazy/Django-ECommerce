from django.contrib import admin
from .models import Product_Image

@admin.register(Product_Image)
class PImagePanel(admin.ModelAdmin):
    list_display = ['image']