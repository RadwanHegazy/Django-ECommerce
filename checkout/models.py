from django.db import models
from users.models import User
from product.models import Product
from uuid import uuid4

class CheckoutGateways(models.Choices) : 
    stripe = 'stripe'
    paymob = 'paymob'


class CheckoutState(models.Choices) : 
    done = 'done'
    failed = 'failed'
    pending = 'pending'


class Checkout(models.Model) :
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, related_name='user_checkout', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='checkout_product', on_delete=models.CASCADE)
    checkout_at = models.DateTimeField(auto_now_add=True)
    checkout_gateway = models.CharField(max_length=10, choices=CheckoutGateways)
    state = models.CharField(max_length=10, choices=CheckoutState, default=CheckoutState.pending.value)
    quantity = models.PositiveIntegerField()
    
    @property
    def total_price (self) : 
        return self.product.price * self.quantity