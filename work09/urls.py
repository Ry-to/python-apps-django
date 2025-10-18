from django.urls import path
from . import views

app_name = "work09"

urlpatterns = [
    path("top/", views.top, name="top"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
]
