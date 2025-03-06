from django.contrib import admin
from django.urls import include, path

from drf_todo.views import TodoAPIView


#dev_drf_todo_1
urlpatterns = [
    path("todo/", TodoAPIView.as_view()),
]
