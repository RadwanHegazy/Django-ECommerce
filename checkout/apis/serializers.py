from rest_framework import serializers
from ..models import Checkout
from global_utills.checkout_packages import stripe_checkout, paymob_checkout

class BaseCheckoutSerializer(serializers.ModelSerializer) :
    checkout_url = None

    class Meta:
        model = Checkout
        fields = ['quantity','product']

    def validate(self, attrs):
        attrs['user'] = self.context.get('user')
        attrs['checkout_gateway'] = self.context.get('checkout_gateway')
        return attrs
    

class StripeCheckoutSerializer(BaseCheckoutSerializer) : 

    def save(self, **kwargs):
        checkout_model = super().save(**kwargs)
        self.checkout_url = stripe_checkout(checkout_model)
    
class PaymobCheckoutSerializer(BaseCheckoutSerializer) : 

    def save(self, **kwargs):
        checkout_model = super().save(**kwargs)
        self.checkout_url = paymob_checkout(checkout_model)