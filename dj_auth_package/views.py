from .serializers import LoginSerializer, ProfileSerializer ,RegisterSerializer, ChangePasswordSerializer, ResetPassword_SentEmailSerializer, ResetPasswordSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

class LoginView (CreateAPIView) : 
    serializer_class = LoginSerializer

class ProfileView (APIView) :
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request) : 
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RegisterView (CreateAPIView) : 
    serializer_class = RegisterSerializer

class ChangePassword (CreateAPIView) : 
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = {
            'user' : self.request.user
        }
        return context

class ResetPasswordOTP(CreateAPIView)  :
    serializer_class = ResetPassword_SentEmailSerializer


class ResetPassowrd (CreateAPIView):
    serializer_class = ResetPasswordSerializer
