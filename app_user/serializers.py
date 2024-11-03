from rest_framework import serializers

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']
