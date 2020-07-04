from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_tasks(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'tasks/tasks.html', context)


def add_language(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_tasks')
            '''
        name = request.POST.get('name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)'''
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'tasks/add_language.html', context)


def edit_language(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_tasks')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'tasks/edit_language.html', context)
