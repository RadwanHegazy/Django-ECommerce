from django.urls import path
from .apis.views import get, create, update, delete


urlpatterns = [
    path('get/<int:id>/',get.GetAllProductComments.as_view(),name='get_product_comments'),
    path('create/<int:id>/',create.CreateProductComments.as_view(),name='create_comment'),
    path('update/<int:id>/',update.UpdateProductComments.as_view(),name='update_comment'),
    path('delete/<int:id>/',delete.DeleteProductComment.as_view(),name='delete_comment'),

]