from django.shortcuts import render

from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    return render(request,'todoapp/index.html', {'todo_list': todos, 'title': 'Main page'})
    
