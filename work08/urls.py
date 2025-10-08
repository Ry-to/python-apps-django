from . import views
from django.urls import path

app_name = "work08"  # これを必ず追加する

urlpatterns = [
    path("top/", views.top, name="top"),
    path("create/", views.create, name="create"),
]
