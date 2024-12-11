from django.contrib import admin
from .models import Checkout, CheckoutProduct

@admin.register(Checkout)
class CheckoutPanel(admin.ModelAdmin) :
    list_display = ['user','total_price','checkout_gateway','state','checkout_at']

@admin.register(CheckoutProduct)
class CheckoutProductPanel (admin.ModelAdmin) : 
    list_display = ['product','quantity','price']