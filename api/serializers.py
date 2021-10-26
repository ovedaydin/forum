from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LikedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Liked
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    get_likes = LikedSerializer(many=True, read_only=True)
    get_likes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
