from django.shortcuts import get_object_or_404
from blog.models import Post
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics


from .mixins import AuthorMixin

    


class PostListApiView(AuthorMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetailApiView(AuthorMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
