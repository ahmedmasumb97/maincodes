from django.urls import path,include
from .import views

urlpatterns = [
    path('add_post/',views.add_post,name='add_post'),
    path('update_post/<int:pk>/',views.update_post,name='update_post'),
    path('delete_post/<int:pk>/',views.delete_post,name='delete_post')
]

