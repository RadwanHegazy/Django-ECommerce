from rest_framework import serializers
from ..models import Checkout

class BaseCheckoutSerializer(serializers.ModelSerializer) :
    
    class Meta:
        model = Checkout
        fields = ['quantity','product']

    def validate(self, attrs):
        attrs['user'] = self.context.get('user')
        attrs['checkout_gateway'] = self.context.get('checkout_gateway')
        return attrs
    

class StripeCheckoutSerializer(BaseCheckoutSerializer) : 

    def save(self, **kwargs):
        super().save(**kwargs)
        return {
            'url' : "STRIPE_CHECKOUT_URL"
        }
    
class PaymobCheckoutSerializer(BaseCheckoutSerializer) : 

    def save(self, **kwargs):
        super().save(**kwargs)
        return {
            'url' : "Paymob_CHECKOUT_URL"
        }
    
