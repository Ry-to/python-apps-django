from django.urls import path

from . import views

urlpatterns = [
    path("top/", views.top, name="top"),
    path("reiwa/", views.reiwa, name="reiwa"),
    path("bmi/", views.bmi, name="bmi"),
    path("warikan/", views.warikan, name="warikan"),
    path("tyokin/", views.tyokin, name="tyokin"),
    path("sisoku/", views.sisoku, name="sisoku"),
]
