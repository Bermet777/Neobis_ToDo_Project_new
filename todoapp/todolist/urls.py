from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    
    path('view/<int:todo_id>/', views.view_task, name='view_task'), 
]