from core.settings.base import STRIPE_REDIRECT_URL, PAYMOB_REDIRECT_URL, STRIPE_TEST_SECRET_KEY, PAYMOB_API_KEY, PAYMOB_MERCHANT_ID,PAYMOB_INTEGERATION_ID, PAYMOB_IFRAME_ID
import stripe, requests
from checkout.models import CheckoutState, Checkout
from .paymob_manager import PaymobManager

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
    
def paymob_checkout(checkout_model:Checkout) -> str:
    """Paymob Checkout""" 
    paymob = PaymobManager()
    images = [i.image.url for i in checkout_model.product.images.all()]
    payment_key = paymob.getPaymentKey(
        currency="EGP",
        amount=checkout_model.product.price,
        user=checkout_model.user,
        integration_id=PAYMOB_INTEGERATION_ID,
        product_image=[{
            "name": checkout_model.product.title,
            "amount_cents": int(checkout_model.product.price * 100),
            "image_url": image_url,
            "description": checkout_model.product.description
        } for image_url in images]
    )
    checkout_url = f"https://accept.paymobsolutions.com/api/acceptance/iframes/{PAYMOB_IFRAME_ID}?payment_token={payment_key}"
    return checkout_url
