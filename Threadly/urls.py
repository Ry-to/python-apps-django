from django.urls import path
from . import views
from .views import PageCreateView, PageDetailView


app_name = "Threadly"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.PageCreateView, name="page_create"),
    path("page/<uuid:pk>/", PageDetailView.as_view(), name="page_detail"),
    path("page/list/", views.PagelistView, name="page_list"),
]
