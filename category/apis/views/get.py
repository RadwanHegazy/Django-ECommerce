from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..serializers import Category, CategorySerializer


class GetAllCategories(ListAPIView) : 
    """Get All Categories"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class RetriveCategoty(RetrieveAPIView) : 
    """Get Category by id"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

