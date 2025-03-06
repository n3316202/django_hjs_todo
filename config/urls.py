from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")), #dev_2 
    path("drf/", include("drf_todo.urls")), #dev_drf_todo_1
    
]
