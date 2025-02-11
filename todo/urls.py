from django.contrib import admin
from django.urls import include, path

from todo import views

#dev_2
urlpatterns = [
    path("", views.todo_list, name="todo_list"),
]
