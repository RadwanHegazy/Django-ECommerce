from rest_framework.views import APIView
from checkout.models import Checkout, CheckoutGateways, CheckoutState
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

class BaseCheckoutView(APIView) : 
    permission_classes = [IsAuthenticated]
    checkout_gateway = None
    serializer_class = None

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
        
    def post(self, request):
        serializer = self.serializer_class(data=request.data,context={
            'user' : request.user,
            'checkout_gateway' : self.checkout_gateway
        })
        if serializer.is_valid() : 
            serializer.save()
            return Response({
                'url' : serializer.checkout_url
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)