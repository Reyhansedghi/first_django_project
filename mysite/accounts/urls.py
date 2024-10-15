from django.urls import path,include
from .views import LogoutView,AuthView,profile

app_name = "accounts"

urlpatterns = [
    path("login", AuthView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("profile", profile, name="profile"),
    path('api/v1/',include('accounts.api.v1.urls')),
]
