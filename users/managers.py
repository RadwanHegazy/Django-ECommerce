from django.contrib.auth.models import BaseUserManager


class CustomUserManager (BaseUserManager) : 

    def create(self, password, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, **kwargs) : 
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self.create(**kwargs)
    
