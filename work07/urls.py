from django.urls import path

from . import views

urlpatterns = [
    path("top/", views.top, name="top"),
    path("omikuji/", views.omikuji, name="omikuji"),
    path("janken/", views.janken, name="janken"),
    path("HiandLow/", views.HiandLow, name="HiandLow"),
]
