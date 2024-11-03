from rest_framework import generics
from rest_framework.views import APIView

from .serializers import *


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = UserModel.objects.all()


class LoginView(APIView):
    serializer_class = LoginSerializer
