from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

@admin.register(User)
class UserPanel (admin.ModelAdmin) : 
    list_display = ['full_name','email','phone']

admin.site.unregister(Group)
