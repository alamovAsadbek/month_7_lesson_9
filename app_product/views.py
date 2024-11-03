from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import *
from .serializers import ProductSerializer


class ProductViewForUser(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    def get_queryset(self):
        return ProductModel.objects.filter(
            status=ProductStatus.active.value
        )


class ProductViewForAdmin(generics.GenericAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return ProductModel.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def put(self, request, *args, **kwargs):
        product = ProductModel.objects.get(id=kwargs['pk'])
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def delete(self, request, *args, **kwargs):
        product = ProductModel.objects.get(id=kwargs['pk'])
        product.status = ProductStatus.deleted.value
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        product = ProductModel.objects.get(id=kwargs['pk'])
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
