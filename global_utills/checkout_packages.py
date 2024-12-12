from core.settings.base import STRIPE_REDIRECT_URL, PAYMOB_REDIRECT_URL, STRIPE_TEST_SECRET_KEY
import stripe
from checkout.models import CheckoutState, Checkout

def url_with_param (url, payment_id, state) : 
    return  url + f"?payment_id={payment_id}&state={state}"

def stripe_checkout(checkout_model:Checkout) -> str:
    """Checkout with stripe and return checkout url""" 
    stripe.api_key = STRIPE_TEST_SECRET_KEY
    product_images = [i.image.url for i in checkout_model.product.images.all()]
    checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': checkout_model.product.title,
                                'images': product_images,  # Optional
                            },
                            'unit_amount': int(checkout_model.product.price * 100),  # Amount in cents
                        },
                        'quantity': checkout_model.quantity,
                    },
                ],
                mode='payment',
                success_url=url_with_param(
                    payment_id = checkout_model.id,
                    state = CheckoutState.done.value,
                    url=STRIPE_REDIRECT_URL
                ),
                cancel_url=url_with_param(
                    payment_id = checkout_model.id,
                    state = CheckoutState.failed.value,
                    url=STRIPE_REDIRECT_URL
                ),
            )
    return checkout_session.url
    
def paymob_checkout(checkout_model:Checkout) : 
    pass