from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(max_length=15, validators=[
        UniqueValidator(queryset=UserModel.objects.all(), message="Phone number already exists")])

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = [{'password': {'write_only': True}}]

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
        elif not phone_number[4:].isdigit():
            raise serializers.ValidationError("Phone number must be a number")

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = UserModel.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
