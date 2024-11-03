from rest_framework import serializers

from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        comment_user = data.get('user')
        if user != comment_user:
            raise serializers.ValidationError("You can only comment on your own posts.")
        return data
