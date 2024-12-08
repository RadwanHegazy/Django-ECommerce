from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductPanel (admin.ModelAdmin) : 
    list_display = ['title','price','quantity','created_at','updated_at']
    list_filter = ['category']
    search_fields = ['title']
    ordering = ['quantity']