from django.urls import path
from .apis.views import get

urlpatterns = [
    path('get/', get.GetProductsView.as_view(),name='get_all_products'),
    path('get/<int:id>/', get.RetriveProductView.as_view(),name='get_product_by_id'),
]