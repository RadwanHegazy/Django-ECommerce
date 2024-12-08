from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Product
from django.core.cache import cache

@receiver(post_save, sender=Product)
def HandProductPrice_Discount(created, instance:Product, **kwargs) : 
    cache.delete('products')
    if not created:
        return
    
    if instance.discount <= 0:
        return
    
    discount_amount = float(instance.discount / 100) * instance.price
    discounted_price = instance.price - discount_amount
    
    instance.price = float(discounted_price)
    instance.save()
