from .base import BaseCheckoutView, CheckoutGateways, Response, status

class StripeCheckoutView(BaseCheckoutView) : 
    checkout_by = CheckoutGateways.stripe.value

    def post(self, request):
        return Response({
            'url' : 'STRIPE_CHECKOUT_URL'
        }, status=status.HTTP_201_CREATED)