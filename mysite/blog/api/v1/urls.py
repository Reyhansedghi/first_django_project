from django.urls import path,include
from .views import PostListApiView, PostDetailApiView
app_name='blog'


urlpatterns = [
    path("posts/", PostListApiView.as_view(), name="post_list_api"),
    path("post/<int:pk>", PostDetailApiView.as_view()),
]