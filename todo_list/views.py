from django.shortcuts import render, redirect
from .models import List
from .forms import listForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = listForm(request.POST or home)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request, ('Item has been added todo list'))
            return render(request, 'home.html', {'all_items': all_items})
            
    else :
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, ('Item has been Deleted'))
    return redirect('home')

def cross_line(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross_line(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk = list_id)
        form = listForm(request.POST or home , instance = item)
        
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been Edited'))
            return redirect('home')

    else:
            item = List.objects.get(pk = list_id)
            return render(request, 'edit.html', {'item': item})