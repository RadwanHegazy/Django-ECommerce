from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..serializers import Product, ReadProductSerializer
from django.core.cache import cache
from datetime import timedelta
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class GetProductsView (ListAPIView) : 
    """Get All Products"""
    serializer_class = ReadProductSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend )
    search_fields = ['title','description']
    filterset_fields = ['category']
    
    def get_queryset(self):
        query = cache.get('products', None)

        if not query : 
            query = Product.objects.filter(quantity__gt=0).order_by('-created_at')
            cache.set(
                'products',
                query,
                timedelta(hours=2).total_seconds()
            )
 
        return query


class RetriveProductView (RetrieveAPIView) : 
    """Retrive Product by id"""
    serializer_class = ReadProductSerializer
    lookup_field = 'id'
    queryset = Product.objects.filter(quantity__gt=0)
