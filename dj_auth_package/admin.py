from django.contrib import admin
from .models import ResetPasswordModel

@admin.register(ResetPasswordModel)
class ResetForm (admin.ModelAdmin) : 
    list_display = ['id','created_at','finished_at', 'user']