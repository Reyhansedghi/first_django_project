from django.urls import path
from .views import post_list,post_detail
app_name='blog'
urlpatterns=[
    path('',post_list,name='post_list'),
    path('post/<slug:slug>',post_detail,name='post_detail'),
    path('category/<slug:category_slug>/',post_list,name='categorypost_list'),
    path('tag/<slug:tag_slug>/',post_list,name='tagpost_list'),
   # path('author/<int:author_pk>/',goods_list,name='author_list'),
]