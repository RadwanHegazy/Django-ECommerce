from django.test import TestCase
from global_utills import base_test
from django.urls import reverse

class TestPaymobEndpoint(TestCase) : 

    def setUp(self):
        self.user = base_test.generate_user()
        self.stripe_endpoint =  reverse('paymob_checkout')

    def test_unauthorized_user(self) : 
        response = self.client.get(self.stripe_endpoint)
        self.assertEqual(response.status_code, 401)

    def test_authorized_user(self) :         
        response = self.client.get(self.stripe_endpoint, headers=base_test.generate_headers(self.user))
        self.assertNotEqual(response.status_code, 401)

    def test_POST_invalid_data(self) : 
        data = {}              
        response = self.client.post(self.stripe_endpoint,headers=base_test.generate_headers(self.user), data=data, content_type='application/json')
        self.assertNotEqual(response.status_code, 200)

    def test_POST_undefined_data(self) : 
        data = {
            'quantity' : 1,
            'product': 999
        }              
        response = self.client.post(self.stripe_endpoint,headers=base_test.generate_headers(self.user), data=data, content_type='application/json')
        self.assertNotEqual(response.status_code, 201)

    def test_POST_valid_data(self) : 
        pd = base_test.generate_product()
        data = {
            'quantity' : 1,
            'product': pd.id
        }              
        response = self.client.post(self.stripe_endpoint,headers=base_test.generate_headers(self.user), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
        