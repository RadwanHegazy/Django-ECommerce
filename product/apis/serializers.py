from rest_framework.serializers import ModelSerializer
from product.models import Product
from category.apis.serializers import CategorySerializer
from product_image.serializers import ReaddProductImageSerializer

class ReadProductSerializer (ModelSerializer) : 
    category = CategorySerializer()
    images = ReaddProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
