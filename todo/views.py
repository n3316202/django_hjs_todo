from django.shortcuts import redirect, render

from todo.forms import TodoForm
from todo.models import Todo

# Create your views here.
def todo_list(request): #dev_2
    todos = Todo.objects.filter(complete=False)
    return render(request, "todo/todo_list.html",{"todos": todos})

#dev_3
def todo_post(request):
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'todo/todo_post.html', {'form': form})
#dev_4
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

#dev_5
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})