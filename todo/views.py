from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem, TodoCompletedItem

# Create your views here.
def todoView(request):
    context = {
        'todo_items': TodoItem.objects.all(), 
        'todo_completed_items': TodoCompletedItem.objects.all()
    }
    return render(request, 'index.html', context)

def todoAddItem(request):
    c = request.POST['inputItem']
    a = TodoItem(content = c)
    a.save()
    return HttpResponseRedirect("/todo/")

def todoDeleteItem(request, itemID):
    a = TodoItem.objects.get(id = itemID)
    c = TodoCompletedItem(content = a.content)
    c.save()
    a.delete()    
    return HttpResponseRedirect("/todo/")

def todoUndoItem(request, itemID):
    c = TodoCompletedItem.objects.get(id = itemID)
    a = TodoItem(content = c.content)
    a.save()
    c.delete()    
    return HttpResponseRedirect("/todo/")