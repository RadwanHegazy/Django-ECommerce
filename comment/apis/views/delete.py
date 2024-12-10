from rest_framework.generics import DestroyAPIView
from comment.models import Comment
from global_utills.permissions import IsCommentOwnerOrReadOnly

class DeleteProductComment(DestroyAPIView) :
    """Endpoint for delete comment"""
    permission_classes = [IsCommentOwnerOrReadOnly]
    lookup_field = 'id'
    queryset = Comment.objects.all()
    

    