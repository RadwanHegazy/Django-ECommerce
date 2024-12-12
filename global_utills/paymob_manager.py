import requests
from core.settings import base

class PaymobManager:
    def getPaymentKey(self, amount, currency, integration_id, product_image, user):
        self.user = user
        self.product_image = product_image
        try:
            authanticationToken = self._getAuthanticationToken(api_key=base.PAYMOB_API_KEY)

            orderId = self._getOrderId(
                authanticationToken=authanticationToken,
                amount=str(100 * amount),
                currency=currency,
            )
            paymentKey = self._getPaymentKey(
                authanticationToken=authanticationToken,
                amount=str(100 * amount),
                currency=currency,
                orderId=str(orderId),
                integration_id = integration_id
            )
            return paymentKey
        except Exception as e:
            raise Exception()

    def _getAuthanticationToken(self, api_key):
        response = requests.post(
            "https://accept.paymob.com/api/auth/tokens",
            json={
                "api_key": api_key,
            }
        )
        return response.json()["token"]

    def _getOrderId(self, authanticationToken, amount, currency):
        response = requests.post(
            "https://accept.paymob.com/api/ecommerce/orders",
            json={
                "auth_token": authanticationToken,
                "amount_cents": amount,
                "currency": currency,
                "delivery_needed": False,
                "items": [],
            }
        )
        return response.json()["id"]

    def _getPaymentKey(self, authanticationToken, orderId, amount, currency, integration_id):
        response = requests.post(
            "https://accept.paymob.com/api/acceptance/payment_keys",
            json={
                "expiration": 3600,
                "auth_token": authanticationToken,
                "order_id": orderId,
                "amount_cents": amount,
                "currency": currency,
                "integration_id": integration_id,
                "billing_data": {
                    "first_name": self.user.full_name, 
                    "last_name":'NA', 
                    "email": self.user.email,
                    "phone_number": "NA",
                    "apartment": "NA",  
                    "floor": "NA", 
                    "street": "NA", 
                    "building": "NA", 
                    "shipping_method": "NA", 
                    "postal_code": "NA", 
                    "city": "NA", 
                    "country": "NA", 
                    "state": "NA",
                    
                    }
                }
        )
        return response.json()["token"]

