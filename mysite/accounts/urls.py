from django.urls import path
from .views import LogoutView,AuthView,profile

app_name = "accounts"

urlpatterns = [
    path("login", AuthView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("profile", profile, name="profile"),
]
