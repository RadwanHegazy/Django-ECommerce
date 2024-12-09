from rest_framework.generics import CreateAPIView
from comment.apis.serializers import CreateCommentSerializer
from product.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class CreateProductComments(CreateAPIView) :
    """Endpoint for create comment on products"""
    serializer_class = CreateCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user' : self.request.user,
            'product' : get_object_or_404(Product, id=self.kwargs.get('id'))
        }
    