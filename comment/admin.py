from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentPanel (admin.ModelAdmin) : 
    list_display = ['user','product','datetime']
    list_filter = ['product','user']