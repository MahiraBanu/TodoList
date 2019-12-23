from django.urls import path
from todo import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo,),
    path('delete_todo/<int:Todo_id>/', views.delete_todo, name='delete_todo')

]