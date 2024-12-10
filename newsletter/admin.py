from django.contrib import admin
from .models import Newsletter

@admin.register(Newsletter)
class NewsLetterPanel (admin.ModelAdmin) : 
    list_display = ['title','created_at']