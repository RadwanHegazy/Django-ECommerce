from .base import BaseCheckoutView, CheckoutGateways
from ...serializers import PaymobCheckoutSerializer

class PaymobCheckoutView(BaseCheckoutView) : 
    checkout_gateway = CheckoutGateways.paymob.value
    serializer_class = PaymobCheckoutSerializer
    