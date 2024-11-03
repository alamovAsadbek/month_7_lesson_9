from rest_framework import generics

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

    def get(self, request, *args, **kwargs):
        return ProductModel.objects.all()
