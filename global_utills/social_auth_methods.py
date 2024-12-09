# Social Auth Section
from .cloudinary_utils import set_user_pic
import threading

def fb_save_data(*args, **kwargs) : 
    from users.models import User, LoginByChoices
    user = kwargs['user'] # the incomming user from the social platfrom
    u, _ = User.objects.get_or_create(
        email=user['email'],
        full_name=user['name'],
        login_by = LoginByChoices.facebook.value
    )
    u.save()
    return u

def google_save_data(*args, **kwargs) : 
    from users.models import User, LoginByChoices
    user = kwargs['user'] # the incomming user from the social platfrom
    u, _ = User.objects.get_or_create(
        email=user['email'],
        full_name=user['name'],
        login_by=LoginByChoices.google.value,
    )

    user_google_pic = user.get('picture', None)
    if _ and user_google_pic:
        t = threading.Thread(
            target=set_user_pic,
            args=(
                user_google_pic,
                u,
            )
        )

        t.start()
            
    u.save()
    return u
