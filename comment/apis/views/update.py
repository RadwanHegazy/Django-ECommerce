from rest_framework.generics import UpdateAPIView
from comment.apis.serializers import UpdateCommentSerializer
from comment.models import Comment
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class UpdateProductComments(UpdateAPIView) :
    """Endpoint for create comment on products"""
    serializer_class = UpdateCommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            'user' : self.request.user,
        }
    