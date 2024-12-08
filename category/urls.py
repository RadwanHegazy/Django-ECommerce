from django.urls import path
from .apis.views import get


urlpatterns = [
    path('get/', get.GetAllCategories.as_view(), name='get_all_categories'),
    path('get/<int:id>/', get.RetriveCategoty.as_view(), name='get_category_by_id'),
    
]