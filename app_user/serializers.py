from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(
        max_length=15,
        validators=[UniqueValidator(queryset=UserModel.objects.all(), message="Phone number already exists")]
    )
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def validate_phone_number(self, phone_number: str):
        phone_number = phone_number.strip()
        if not phone_number.startswith('+998'):
            raise serializers.ValidationError("Phone number must start with +998")
        if not phone_number[4:].isdigit():
            raise serializers.ValidationError("Phone number must contain only digits after the country code")
        return phone_number

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove the confirm_password field
        user = UserModel.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])  # Ensure the password is hashed
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(min_length=8, write_only=True)
