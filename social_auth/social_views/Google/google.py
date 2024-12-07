from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from social_auth.platforms import GoogleAuth
from .serializers import GoogleCodeSerializer

class GoogleAuthView(CreateAPIView) :
    serializer_class = GoogleCodeSerializer
    queryset = []

class CreateGoogleAuthLinkView(APIView) :
    __google_auth = GoogleAuth()

    def get (self, request) : 
        return Response({
            'url' : self.__google_auth.get_auth_url()
        })