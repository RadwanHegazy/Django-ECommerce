from rest_framework import serializers
from .models import Product_Image

class ReaddProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = ['image']

    def to_representation(self, instance:Product_Image):
        data = {
            'src' : instance.image.url
        } 
        return data
    