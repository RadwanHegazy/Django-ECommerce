from django.test import TestCase
from .base import generate_comment, generate_headers
from django.urls import reverse

class TestDeleteEndpoint(TestCase) :
    def setUp(self):
        self.comment = generate_comment()
        self.endpoint_url = reverse('delete_comment',args=[self.comment.id])
        return super().setUp()
    
    def test_create_unauthorized_method(self) : 
        response = self.client.delete(self.endpoint_url)
        self.assertEqual(response.status_code, 401)
        
    def test_create_comment_in_notfound_product(self) : 
        repsonse = self.client.delete(reverse('delete_comment', args=[2]),headers=generate_headers())
        self.assertEqual(repsonse.status_code, 404)

    def test_delete_comment_success(self) : 
        response = self.client.delete(self.endpoint_url, headers=generate_headers())
        self.assertEqual(response.status_code, 204)
        
