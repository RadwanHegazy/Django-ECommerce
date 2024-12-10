from django.db import models


class Newsletter(models.Model) : 
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title