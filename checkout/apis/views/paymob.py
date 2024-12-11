from .base import BaseCheckoutView, CheckoutGateways, Response, status

class PaymobCheckoutView(BaseCheckoutView) : 
    checkout_by = CheckoutGateways.paymob.value

    def post(self, request):
        return Response({
            'url' : 'PAYMOB_CHECKOUT_URL'
        }, status=status.HTTP_201_CREATED)