from rest_framework import serializers
from blog.models import Post
from services.models import Services
from products.models import Product
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

class ProductOrServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # or Service, it doesn't matter which one we choose
        fields = '__all__'

    def to_representation(self, instance):
        if isinstance(instance, Product):
            return ProductSerializer(instance).data
        elif isinstance(instance, Services):
            return ServiceSerializer(instance).data





