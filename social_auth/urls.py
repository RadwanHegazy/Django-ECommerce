from django.urls import path
from social_auth.social_views.Google import google
from social_auth.social_views.Facebook import facebook
# from social_auth.social_views.Github import github

urlpatterns = [
    path('google/', google.GoogleAuthView.as_view()),
    path('google/url/', google.CreateGoogleAuthLinkView.as_view()),

    path('facebook/', facebook.FacebookAuthView.as_view()),
    path('facebook/url/',facebook.CreateFacebookAuthLinkView.as_view()),
    
    # path('github/', github.GithubAuthView.as_view()),
    # path('github/url/',github.CreateGithubAuthLinkView.as_view()),
]
