from django.shortcuts import get_object_or_404
from blog.models import Post
from services.models import Services
from products.models import Product
from itertools import chain
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from . serializers import PostSerializer,ProductSerializer,ProductOrServiceSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .mixins import AuthorMixin
class PostListApiView(AuthorMixin,generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductOrServiceSerializer

    def get_queryset(self):
        products = Product.objects.all()
        services = Services.objects.all()
        return chain(products, services)
    def perform_create(self, serializer):
        data = self.request.data
        if data.get('type') == 'product':
            serializer.save(instance=Product())
        elif data.get('type') == 'service':
            serializer.save(instance=Services())
        else:
            raise ValueError('Invalid type')


class ProductOrServiceDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductOrServiceSerializer

    def get_queryset(self):
        if self.kwargs['object_type'] == 'product':
            return Product.objects.all()
        elif self.kwargs['object_type'] == 'service':
            return Services.objects.all()
        else:
            raise ValueError('Invalid object type')