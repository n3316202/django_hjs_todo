from django.contrib import admin
from django.urls import include, path

from todo import views

# dev_2
urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("post/", views.todo_post, name="todo_post"),  # dev_3
    path("<int:pk>/", views.todo_detail, name="todo_detail"),  # dev_4
    path("<int:pk>/edit/", views.todo_edit, name="todo_edit"),  # dev_5
    path("done/", views.done_list, name="done_list"),  # dev_6
    path("done/<int:pk>/", views.todo_done, name="todo_done"),  # dev_6
]
