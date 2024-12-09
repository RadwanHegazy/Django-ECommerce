from django.test import TestCase
from .base import generate_headers, generate_comment, generate_product
from django.urls import reverse

class TestCreateEndpoint(TestCase) :

    def setUp(self):
        self.product = generate_product()
        self.endpoint_url = reverse('create_comment',args=[self.product.id])
        return super().setUp()
    
    def test_create_unauthorized_method(self) : 
        response = self.client.post(self.endpoint_url)
        self.assertEqual(response.status_code, 401)
        
    def test_create_comment_in_notfound_product(self) : 
        repsonse = self.client.post(reverse('create_comment', args=[2]),headers=generate_headers())
        self.assertEqual(repsonse.status_code, 404)

    def test_create_comment_no_data(self) : 
        response = self.client.post(self.endpoint_url, headers=generate_headers())
        self.assertNotEqual(response.status_code, 201)
        

    def test_create_comment_success(self) : 
        response = self.client.post(self.endpoint_url, headers=generate_headers(),data={
            'content' : 'test content'
        })
        self.assertEqual(response.status_code, 201)
        
