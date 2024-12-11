from django.contrib import admin
from .models import Checkout

@admin.register(Checkout)
class CheckoutPanel(admin.ModelAdmin) :
    list_display = ['user','total_price','checkout_gateway','state','checkout_at']
    list_filter = ['checkout_gateway', 'state']

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False
    
    def has_delete_permission(self, request, obj = ...):
        return False
