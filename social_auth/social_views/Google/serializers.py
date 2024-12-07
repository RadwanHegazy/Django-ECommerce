from rest_framework import serializers
from social_auth.platforms import GoogleAuth, generate_tokens_for_user
from django.contrib.auth import get_user_model

User = get_user_model()

class GoogleCodeSerializer (serializers.Serializer) : 
    code = serializers.CharField()
    __google_auth = GoogleAuth()
    
    def create(self, validated_data):
        code = validated_data.get('code')
        user = self.__google_auth.get_user_info_by_code(code)
        site_user = self.__google_auth.save_user_data(user_dict=user)
        return site_user
    
    def to_representation(self, instance):
        tokens = generate_tokens_for_user(instance)
        return tokens

