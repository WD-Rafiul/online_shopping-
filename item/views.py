from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm

# Create your views here.

from . models import Items, Category
def details (request,pk):
    item = get_object_or_404(Items, pk=pk)
    related_items = Items.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[:3]
    return render(request, 'item/detail.html',{'item':item ,'related_items':related_items})


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk = item.id)

    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {'form': form , 'title':'Add new item'})

@login_required
def edit(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():

            item.save()
            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title':'Edit item'
        })
    

@login_required
def delete(request, pk):
    item = get_object_or_404(Items, pk=pk, created_by= request.user)
    item.delete()

    return redirect('deshboard:index')


def items(request):
    items=Items.objects.filter(is_sold=False)
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id = category_id)


    return render(request, 'item/items.html', {
        'items': items,
        'categories': categories,
        'category_id':category_id,
        })