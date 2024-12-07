from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken

class TestEndpoints (TestCase) :

    def create_test_user(self) :
        u = self.user.objects.create(
            phone='+201009675224',
            email='test@gmail.com',
        )
        u.set_password('test')
        u.save()
        return u
    
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('auth_login')
        self.profile_url = reverse('profile')
        self.register_url = reverse('auth_register')
        self.update_user_password = reverse('change_password')
        self.user = get_user_model()

    def test_login_endpoint_no_data(self) : 
        response = self.client.post(self.login_url,data={})
        self.assertEqual(response.status_code, 400)
    
    def test_login_endpoint_valid_data(self) : 
        u = self.create_test_user()
        response = self.client.post(self.login_url,data={
            'email' : 'test@gmail.com',
            'password' : 'test',
        })
        self.assertEqual(response.status_code, 201)
    
    def test_register_endpoint_already_username_exists (self) : 
        u = self.create_test_user()
        response = self.client.post(self.register_url, data={
            'email' : 'test2@gmail.com',
            'password' : 'test',
            'phone' : '+201009674001',
        })
        self.assertNotEqual(response.status_code, 201)

    def test_register_endpoint_success (self) : 
        response = self.client.post(self.register_url, data={
            'email' : 'test2@gmail.com',
            'password' : 'test',
            'phone' : '+201009674001',
            'full_name' : "Testing"
        })
        self.assertEqual(response.status_code, 201)

    def test_change_password_endpoint_sucess (self) : 
        u = self.create_test_user()
        response = self.client.post(self.update_user_password,headers={
            'Authorization' : f"Bearer {AccessToken.for_user(u)}"
        }, data={
            'old_password' : 'test',
            'password' : 'new_test',
            'password2' : 'new_test'
        })
        self.assertEqual(response.status_code, 201)

    def test_change_password_no_headers(self) : 
        u = self.create_test_user()
        response = self.client.post(self.update_user_password, data={
            'old_password' : 'test',
            'password' : 'new_test',
            'password2' : 'new_test'
        })
        self.assertNotEqual(response.status_code, 201)

    def test_change_password_no_data(self) : 
        u = self.create_test_user()
        response = self.client.post(self.update_user_password,headers={
            'Authorization' : f"Bearer {AccessToken.for_user(u)}"
        })
        self.assertNotEqual(response.status_code, 201)

    def test_profile_endpoint (self) : 
        user = self.create_test_user()
        access_token = AccessToken.for_user(user)
        response = self.client.get(self.profile_url,headers={
            'Authorization' : f"Bearer {access_token}"
        })
        
        self.assertEqual(response.status_code, 200)