from django.urls import path,include
from .import views

urlpatterns = [
    path('add_author/',views.add_author,name='add_author'),
    path('task_list/',views.task_list,name='task_list'),
    path('task_details/<int:pk>/',views.task_details,name='task_details'),
    path('task_delete/<int:pk>/',views.delete_task,name='task_delete'),
    path('task_update/<int:pk>/',views.update_task,name='task_update'),
    path('author_details/',views.author_details,name='author_datails')
]
