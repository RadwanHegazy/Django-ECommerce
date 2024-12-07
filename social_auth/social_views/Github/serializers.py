from rest_framework import serializers
from social_auth.platforms import GitHubAuth, generate_tokens_for_user
from django.contrib.auth import get_user_model

User = get_user_model()

class GithubCodeSerializer (serializers.Serializer) : 
    code = serializers.CharField()
    __github_auth = GitHubAuth()
    
    def create(self, validated_data):
        code = validated_data.get('code')
        access_token = self.__github_auth.get_access_token(code)
        user = self.__github_auth.get_user_by_access_token(access_token)
        site_user = self.__github_auth.save_user_data(user_dict=user)

        return site_user
    
    def to_representation(self, instance):
        tokens = generate_tokens_for_user(instance)
        return tokens

