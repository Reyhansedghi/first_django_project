from django.urls import path,include
from .views import PostListApiView, ProductOrServiceDetailApiView
app_name='blog'


urlpatterns = [
    path("posts/", PostListApiView.as_view(), name="post_list_api"),
    path('post/<str:object_type>/<int:pk>/', ProductOrServiceDetailApiView.as_view(), name='product-or-service-detail'),
]