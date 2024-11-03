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
