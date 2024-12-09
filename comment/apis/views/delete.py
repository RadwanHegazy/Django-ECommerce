from rest_framework.generics import DestroyAPIView
from comment.models import Comment
from rest_framework.permissions import IsAuthenticated

class DeleteProductComment(DestroyAPIView) :
    """Endpoint for delete comment"""
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = Comment.objects.all()
    

    