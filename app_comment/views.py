from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class CommentView(generics.GenericAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
