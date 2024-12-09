from rest_framework import serializers
from ..models import Comment
from rest_framework.exceptions import ValidationError
from users.models import User

class UserCommentSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = User
        fields = ["id",'picture','full_name']

    def to_representation(self, instance:User):
        data = super().to_representation(instance)
        data['picture'] = instance.picture.url if instance.picture else None
        return data

class ReadOnlyCommentSerializer (serializers.ModelSerializer) : 
    user = UserCommentSerializer()

    class Meta:
        model = Comment
        fields = "__all__"

    
class CreateCommentSerializer (serializers.ModelSerializer) :

    class Meta:
        model = Comment
        fields = ['id','content']
        
    def validate(self, attrs):
        user = self.context.get('user', None)
        product = self.context.get('product', None)
        
        if not user:
            ValidationError({
                'message' : 'user must be inserted'
            })

        if not product : 
            ValidationError({
                'message' : 'product must be inserted'
            })
            
        attrs['user'] = user
        attrs['product'] = product
        return attrs  
    
class UpdateCommentSerializer (serializers.ModelSerializer) :

    class Meta:
        model = Comment
        fields = ['id','content']

    def update(self, instance, validated_data):
        for key, val in validated_data.items():
            setattr(instance, key, val)
        instance.save()
        return instance