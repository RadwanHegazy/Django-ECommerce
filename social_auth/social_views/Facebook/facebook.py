from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from social_auth.platforms import FacebookAuth
from .serializers import FacebookSerializer

class FacebookAuthView(CreateAPIView) :
    serializer_class = FacebookSerializer
    queryset = []


class CreateFacebookAuthLinkView(APIView) :
    __fb_auth = FacebookAuth()

    def get (self, request) : 
        return Response({
            'url' : self.__fb_auth.get_auth_url()
        })