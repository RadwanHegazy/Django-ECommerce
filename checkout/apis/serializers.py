from rest_framework import serializers
from ..models import Checkout

class StripeCheckoutSerializer(serializers.ModelSerializer) :
    products = serializers.ListField()

    def validate(self, attrs):
        attrs['user'] = self.context.get('user')
        return attrs
    
    