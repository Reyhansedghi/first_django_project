from django.urls import path
from .views import PostList,DashBoard

app_name = "accounts"

urlpatterns = [
    path("", DashBoard.as_view(), name="dashbourd"),
    path("postslist", PostList.as_view(), name="post_list"),
    
]