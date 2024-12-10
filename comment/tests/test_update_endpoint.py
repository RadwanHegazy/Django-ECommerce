from django.test import TestCase
from global_utills.base_test import generate_headers, generate_comment, generate_user
from django.urls import reverse

class TestGetEndpoint(TestCase) :
    def setUp(self):
        self.comment = generate_comment()
        self.endpoint_url = reverse('update_comment',args=[self.comment.id])
        return super().setUp()
    
        
    def test_create_unauthorized_method(self) : 
        response = self.client.put(self.endpoint_url)
        self.assertEqual(response.status_code, 401)
        
    def test_create_comment_in_notfound_product(self) : 
        repsonse = self.client.put(reverse('update_comment', args=[2]),headers=generate_headers())
        self.assertEqual(repsonse.status_code, 404)

    def test_update_comment_no_data(self) : 
        response = self.client.put(self.endpoint_url, headers=generate_headers())
        self.assertNotEqual(response.status_code, 201)
        

    def test_update_comment_no_permissions(self) : 
        response = self.client.put(self.endpoint_url, headers=generate_headers(),data={
            'content' : 'updated test content'
        }, content_type='application/json')
        self.assertEqual(response.status_code, 403)
        
    def test_update_comment_has_permissions(self) : 
        response = self.client.put(self.endpoint_url, headers=generate_headers(user=self.comment.user),data={
            'content' : 'updated test content'
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
