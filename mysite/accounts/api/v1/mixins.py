from blog.models import Post
from services.models import Services
from products.models import Product
from .serializers import PostSerializer
from itertools import chain
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from . serializers import PostSerializer,ProductSerializer,ServiceSerializer

class AuthorMixin:
    def get_queryset(self):
        user = self.request.user
        products=Product.objects.filter(user=user)
        services=Services.objects.filter(user=user)

        return list(chain(products, services))
    
class DetailMixin:
        
    def get_queryset(self):
        user = self.request.user
        products=Product.objects.filter(user=user)
        services=Services.objects.filter(user=user)

        return list(chain(products, services))
        