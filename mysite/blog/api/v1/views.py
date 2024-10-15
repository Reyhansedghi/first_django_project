from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework import generics
from .mixins import AuthorMixin
class PostListApiView(AuthorMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetailApiView(AuthorMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
