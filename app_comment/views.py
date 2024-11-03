from rest_framework import generics


class CommentView(generics.GenericAPIView):
    serializer_class = CommentSerializer
