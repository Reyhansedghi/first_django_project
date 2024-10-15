from django.shortcuts import get_object_or_404
from services.models import Services
from products.models import Product
from itertools import chain
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from . serializers import ProductOrServiceSerializer
from rest_framework import generics
class PostListApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductOrServiceSerializer

    def get_queryset(self):
        user = self.request.user
        products=Product.objects.filter(user=user)
        services=Services.objects.filter(user=user)
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
        user = self.request.user
        if self.kwargs['object_type'] == 'product':
            return Product.objects.filter(user=user)
        elif self.kwargs['object_type'] == 'service':
            return Services.objects.filter(user=user)
        else:
            raise ValueError('Invalid object type')