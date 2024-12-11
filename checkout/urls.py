from .apis.views import paymob, stripe
from django.urls import path

urlpatterns = [
    path('stripe/', stripe.StripeCheckoutView.as_view(),name='stripe_checkout'),
    path('paymob/', paymob.PaymobCheckoutView.as_view(),name='paymob_checkout'),
]