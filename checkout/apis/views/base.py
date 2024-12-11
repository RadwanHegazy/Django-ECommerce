from rest_framework.views import APIView
from checkout.models import Checkout, CheckoutGateways, CheckoutState
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

class BaseCheckoutView(APIView) : 
    checkout_by = None
    permission_classes = [IsAuthenticated]

    def post(self, request) : 
        """Must Return the checkout url"""
        pass


    def get(self, request) :
        payment_id = request.GET.get('payment_id', None)
        state = request.GET.get('state', None)

        if not payment_id or not state or state not in CheckoutState:
            raise ValidationError("Invalid Action")
        
        try : 
            payment = Checkout.objects.get(id=payment_id)
            payment.state = state
            payment.save()
            return Response({
                'message' : 'Payment done'
            }, status=status.HTTP_200_OK)
        except Checkout.DoesNotExist:
            raise ValidationError("Checkout Not Found ")
        