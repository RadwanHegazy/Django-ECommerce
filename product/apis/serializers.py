from rest_framework.serializers import ModelSerializer
from product.models import Product
from category.apis.serializers import CategorySerializer

class ReadProductSerializer (ModelSerializer) : 
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"
