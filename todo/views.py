from django.shortcuts import render

from todo.models import Todo

# Create your views here.
def todo_list(request): #dev_2
    todos = Todo.objects.filter(complete=False)
    return render(request, "todo/todo_list.html",{"todos": todos})