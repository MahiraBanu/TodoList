from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from todo.models import Todo_List

# Create your views here.

def index(request):
    item_list = Todo_List.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'todo_items': item_list})


def add_todo(request):
    added_date = timezone.now()
    text = request.POST['task']
    Todo_List.objects.create(pub_date=added_date, task=text)
    
    return HttpResponseRedirect('/')


def delete_todo(request, Todo_id):
    Todo_List.objects.get(id=Todo_id).delete()
    return HttpResponseRedirect('/')
