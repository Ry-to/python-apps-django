from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
