from django.urls import path
from . import views


app_name = "todo"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
    path("pages/", views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.PageDetailView.as_view(), name="page_detail"),
    path("page/<uuid:id>/update/", views.PageUpdateView.as_view(), name="page_update"),
    path("page/<uuid:id>/delete/", views.PageDeleteView.as_view(), name="page_delete"),
    path("page/<uuid:id>/done/", views.PageDoneView.as_view(), name="page_done"),
]
