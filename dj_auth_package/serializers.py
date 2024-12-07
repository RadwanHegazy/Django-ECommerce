from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from .models import ResetPasswordModel
from .utils import send_reset_password_email
from datetime import datetime
from django.db.models.fields.files import ImageFileDescriptor

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = User
        exclude = ['password']

class BaseSerialzer (serializers.Serializer) :
    password = serializers.CharField(write_only=True, style={'input_type':'password'})

    def to_representation(self, *args, **kwargs):
        tokens = RefreshToken.for_user(self.user)
        data = {
            'refresh_token' : str(tokens),
            'access_token' : str(tokens.access_token),
        }
        return data

class LoginSerializer (BaseSerialzer) :
    user = None
    
    def __init__(self, *args, **kwargs) : 
        super().__init__(*args, **kwargs)    
        self.fields[User.USERNAME_FIELD] = serializers.CharField()

    def validate(self, attrs):
        psd = attrs.pop('password')

        try : 
            self.user = User.objects.get(**attrs)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : f'invalid {User.USERNAME_FIELD}'
            })
        
        if not self.user.check_password(psd) : 
            raise ValidationError({
                'message' : 'invalid password'
            })
        
        return attrs
    
    def create(self, validated_data):
        return self.user

class RegisterSerializer (BaseSerialzer) : 

    def __init__(self, *args, **kwargs) : 
        super().__init__(*args, **kwargs)
        self.custom_fields = User.REQUIRED_FIELDS + [User.USERNAME_FIELD]
        for field in self.custom_fields:
            if type(getattr(User,field)) == ImageFileDescriptor:
                self.fields[field] = serializers.ImageField()
            else:
                self.fields[field] = serializers.CharField()
    
    def validate(self, attrs) : 
        username_field = attrs.get(self.custom_fields[-1])

        try :
            user = User.objects.get(**{self.custom_fields[-1] : username_field})
            raise ValidationError({
                'message' : f'this {self.custom_fields[-1]} already exists'
            })
        except User.DoesNotExist:
            pass

        return attrs
    
    def create(self, validated_data):
        self.user = User.objects.create_user(**validated_data)
        return self.user

class ChangePasswordSerializer(BaseSerialzer):
    password2 = serializers.CharField(write_only=True, style={'input_type':'password'})
    old_password = serializers.CharField(write_only=True, style={'input_type':'password'})

    def validate(self, attrs):
        psd1 = attrs.get('password')
        psd2 = attrs.get('password2')
        old_password = attrs.get('old_password')
        self.user = self.context.get('user')

        if not self.user.check_password(old_password) : 
            raise ValidationError({
                'message' : 'wrong old password'
            })
        
        if psd1 != psd2 : 
            raise ValidationError({
                'message' : 'two passwords did not matches'
            })
        
        validate_password(psd1)

        self.user.set_password(psd1)
        self.user.save()

        return attrs
    
    def create(self, *args, **kwargs):
        return self.user
    
class ResetPassword_SentEmailSerializer(serializers.Serializer) : 
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')

        try : 
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : 'user with this email not exists'
            })

        return attrs
    
    def create(self, validated_data):
        model = ResetPasswordModel.objects.create(
            user=self.user
        )
        model.save()
        send_reset_password_email(
            to_user_email=self.user.email,
            otp_code=model.otp_code
        )
        return model
    
    def to_representation(self, instance):
        return {
            "message" : 'email sent successfully'
        }

class ResetPasswordSerializer (BaseSerialzer) : 
    password2 = serializers.CharField(write_only=True, style={'input_type':'password'})
    otp_code = serializers.IntegerField()

    def validate(self, attrs):
        psd1 = attrs.get('password')
        psd2 = attrs.get('password2')
        otp_code = attrs.get('otp_code')
        

        try : 
            form_model = ResetPasswordModel.objects.get(otp_code=otp_code,finished_at__gt=datetime.now())
        except ResetPasswordModel.DoesNotExist:
            raise ValidationError({
                'message' : 'invalid otp code'
            })
        
        
        if psd1 != psd2 :
            raise ValidationError({
                'message' : 'two password field didn not matches'
            })
        
        validate_password(psd1)

        self.user = form_model.user
        self.user.set_password(psd1)

        form_model.delete()

        return attrs
    
    def create(self, *args, **kwaargs):
        return self.user