import os
from global_utills import social_auth_methods

SOCIAL_AUTH = {
    
    'google' : {
        'client_id' : os.getenv('GOOGLE_CLIENT_ID'),
        'client_secret' : os.getenv('GOOGLE_CLIENT_SECRET'),
        'redirect_url' : 'http://localhost:8000/auth/google/', # your frontend server
        'save_user_data' : social_auth_methods.google_save_data
    },
    
    'facebook' : {
        'client_id' : os.getenv('FB_CLIENT_ID'),
        'client_secret' : os.getenv('FB_CLIENT_SECRET'),
        'redirect_url' : 'http://localhost:8000/user/social/facebook/', # your frontend server,
        'save_user_data' : social_auth_methods.fb_save_data

    },

    # NOTE: Set it blank because i'm not gonna use it
    'github' : {
        'client_id' : '',
        'client_secret' : '',
        'redirect_url' : '', # your frontend server
        'save_user_data' : None
    }


}