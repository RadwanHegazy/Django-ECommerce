from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryPanel(admin.ModelAdmin): 
    list_display = ['name','created_at','updated_at']