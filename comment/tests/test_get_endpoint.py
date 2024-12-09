from django.test import TestCase
from django.urls import reverse
from .base import generate_product, generate_comment

class TestGetEndpoint(TestCase) :
    
    def setUp(self):
        self.product = generate_product()
        self.get_endpoint_url = reverse('get_product_comments',args=[self.product.id])
        return super().setUp()
    
    def test_get_success_endpoint(self) : 
        response = self.client.get(self.get_endpoint_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

    def test_get_notfound_endpoint(self) : 
        repsonse = self.client.get(reverse('get_product_comments', args=[2]))
        self.assertEqual(repsonse.status_code, 404)


    def test_get_non_empty_comments(self) : 
        comment = generate_comment()
        product  = comment.product
        repsonse = self.client.get(reverse('get_product_comments', args=[product.id]))
        self.assertNotEqual(len(repsonse.json()), 0)
        
