from rest_framework.generics import ListAPIView
from comment.apis.serializers import Comment, ReadOnlyCommentSerializer
from product.models import Product
from rest_framework.exceptions import NotFound

class GetAllProductComments(ListAPIView) :
    """Endpoint for getting all product comments"""
    serializer_class = ReadOnlyCommentSerializer
    
    def get_queryset(self):
        product_id = self.kwargs.get('id')

        try : 
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound("Product not found")
        
        return Comment.objects.filter(
            product=product
        )
