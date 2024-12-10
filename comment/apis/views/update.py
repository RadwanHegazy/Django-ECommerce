from rest_framework.generics import UpdateAPIView
from comment.apis.serializers import UpdateCommentSerializer
from comment.models import Comment
from global_utills.permissions import IsCommentOwnerOrReadOnly

class UpdateProductComments(UpdateAPIView) :
    """Endpoint for create comment on products"""
    serializer_class = UpdateCommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'
    permission_classes = [IsCommentOwnerOrReadOnly]
    

    def get_serializer_context(self):
        return {
            'user' : self.request.user,
        }
    