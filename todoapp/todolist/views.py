from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    return render(request,'todoapp/index.html', {'todo_list': todos, 'title': 'Main page'})
    
@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    todo = ToDo(title=title, description=description)
    todo.save()
    return redirect('index')

def edit(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        todo.title = title
        todo.description = description
        todo.save()
        return redirect('index')
    return render(request, 'todoapp/edit.html', {'todo': todo})

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


def view_task(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    return render(request, 'todoapp/view_task.html', {'todo': todo})