"""
    ALl avaliable platforms for implement social auth
"""

from abc import ABC, abstractmethod
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.exceptions import ValidationError
import requests
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class BaseSocialPlatform(ABC) : 
    
    @abstractmethod
    def get_access_token(self) : ...

    @abstractmethod
    def get_auth_url(self) : ...

    @abstractmethod
    def save_user_data(self) : ...


def generate_tokens_for_user(user) -> dict:
    tokens = RefreshToken.for_user(user)

    return {
        'refresh_token':str(tokens),
        'access_token' : str(tokens.access_token) 
    }

class GoogleAuth(BaseSocialPlatform) : 
    GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
    GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
    GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'
    GOOGLE_SOCIAL_AUTH = settings.SOCIAL_AUTH['google']
    GOOGLE_REDIRECT_URL = GOOGLE_SOCIAL_AUTH['redirect_url']
    SAVE_USER_DATA_FUNCTION = GOOGLE_SOCIAL_AUTH['save_user_data']

    def get_access_token(self, code):
        data = {
            'code': code,
            'client_id': self.GOOGLE_SOCIAL_AUTH['client_id'],
            'client_secret': self.GOOGLE_SOCIAL_AUTH['client_secret'],
            'redirect_uri': self.GOOGLE_REDIRECT_URL,
            'grant_type': 'authorization_code'
        }

        response = requests.post(self.GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)

        if not response.ok : 
            raise ValidationError('Failed to get access token from google')

        json_data = response.json()
        return json_data['access_token']
    
    def get_user_info_by_code(self, code):
        access_token = self.get_access_token(code) 
        response = requests.get(
            self.GOOGLE_USER_INFO_URL,
            params={'access_token' : access_token}
        )

        if not response.ok :
            raise ValidationError("Failed to get user information with tokens from google")
        
        return response.json()

    def get_auth_url(self):
        client_id = self.GOOGLE_SOCIAL_AUTH['client_id']
        url = f"https://accounts.google.com/o/oauth2/v2/auth?scope=email%20profile&access_type=offline&redirect_uri={self.GOOGLE_REDIRECT_URL}&response_type=code&client_id={client_id}"
        return url

    def save_user_data(self, user_dict)  :
        user = self.SAVE_USER_DATA_FUNCTION(user=user_dict)
        return user
    
class FacebookAuth(BaseSocialPlatform):
    FB_SOCIAL_AUTH = settings.SOCIAL_AUTH['facebook']
    FB_REDIRECT_URL = FB_SOCIAL_AUTH['redirect_url']
    FB_CLIENT_ID = FB_SOCIAL_AUTH['client_id']
    FB_CLIENT_SECRET = FB_SOCIAL_AUTH['client_secret']
    SAVE_USER_DATA_FUNCTION = FB_SOCIAL_AUTH['save_user_data']

    def get_access_token(self):...

    def get_auth_url(self):
        url = f"https://www.facebook.com/v14.0/dialog/oauth?client_id={self.FB_CLIENT_ID}&redirect_uri={self.FB_REDIRECT_URL}&scope=email,public_profile,user_friends&response_type=token"
        return url
    
    def get_user_info_by_accessToken(self, access_token) :
        url = f'https://graph.facebook.com/me?access_token={access_token}&fields=id,name,email'
        response = requests.get(url)
        
        if not response.ok :
            raise ValidationError({'error': 'Invalid token.'})
        
        user_info = response.json()
        return user_info
    
    def save_user_data(self, user_dict)  :
        user = self.SAVE_USER_DATA_FUNCTION(user=user_dict)
        return user
    

class GitHubAuth (BaseSocialPlatform) :
    GITHUB_SOCIAL_AUTH = settings.SOCIAL_AUTH['github']
    GITHUB_REDIRECT_URL = GITHUB_SOCIAL_AUTH['redirect_url']
    GITHUB_CLIENT_ID = GITHUB_SOCIAL_AUTH['client_id']
    GITHUB_CLIENT_SECRET = GITHUB_SOCIAL_AUTH['client_secret']
    SAVE_USER_DATA_FUNCTION = GITHUB_SOCIAL_AUTH['save_user_data']


    def get_access_token(self, code):
        token_response = requests.post(
            'https://github.com/login/oauth/access_token',
            headers={'Accept': 'application/json'},
            data={
                'client_id': self.GITHUB_CLIENT_ID,
                'client_secret': self.GITHUB_CLIENT_SECRET,
                'code': code
                }
            )

        if not token_response.ok:
            raise ValidationError("Invalid Code")
        
        token_json = token_response.json()
        access_token = token_json.get('access_token', None)

    
        return access_token
    
    def get_user_by_access_token(self, access_token) :
        user_response = requests.get(
            'https://api.github.com/user',
            headers={'Authorization': f'token {access_token}'}
        )
        if not user_response.ok :
            raise ValidationError("Invalid Access Token")
        
        user_info = user_response.json()
        return user_info
    

    def get_auth_url(self):
        url = f"https://github.com/login/oauth/authorize?client_id={self.GITHUB_CLIENT_ID}&redirect_uri={self.GITHUB_REDIRECT_URL}&scope=user:email"
        return url
    
    def save_user_data(self, user_dict)  :
        user = self.SAVE_USER_DATA_FUNCTION(user=user_dict)
        return user
    