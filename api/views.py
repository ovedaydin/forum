from django.shortcuts import render

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class PostView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        try:
            posts = Post.objects.all().order_by('-created_at')
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        except:
            return Response({"message": "There's no data"})

    def post(self, request, format=None):
        if request.data:
            try:
                id = request.data["id"]
                object = Post.objects.get(id=id)
                if object.user == request.user:
                    serializer = PostSerializer(object, data=request.data, partial=True)
                else:
                    return Response({"message": "You cannot update this post"})
            except:
                serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({"message": "There's no data"})


class PostDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, *args, **kwargs):
        try:
            id = kwargs["id"]
            object = Post.objects.get(id=id)
            if object.user == request.user:
                object.delete()
                return Response({"message": "deleted"})
            return Response({"message": "You cannot delete this post"})
        except:
            return Response({"message": "There's no related data in body"})


class LikedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, *args, **kwargs):
        try:
            post = Post.objects.get(id=kwargs["id"])
            serializer = LikedSerializer(data={"user": request.user.id,
                                               "post": kwargs["id"]})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response({"message": "There's no post with the id"})


class DislikedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, *args, **kwargs):

        try:
            like = Liked.objects.get(post=kwargs["id"])
            like.delete()
            return Response({"message": "disliked"})
        except:
            return Response({"message": "There's no post with the id"})
