from .base import BaseCheckoutView, CheckoutGateways
from ...serializers import StripeCheckoutSerializer

class StripeCheckoutView(BaseCheckoutView) : 
    """View for stripe payment only"""
    checkout_gateway = CheckoutGateways.stripe.value
    serializer_class = StripeCheckoutSerializer