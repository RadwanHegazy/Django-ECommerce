from django.db import models
from users.models import User
from product.models import Product

class Comment(models.Model) : 
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_comments', on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
