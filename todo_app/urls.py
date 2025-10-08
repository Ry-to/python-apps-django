from . import views
from django.urls import path

urlpatterns = [
    path("todo/", views.todo, name="todo"),
    path("create/", views.create, name="create"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle_task"),
]
