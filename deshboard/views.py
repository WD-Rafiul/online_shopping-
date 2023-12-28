from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Items
# Create your views here.


@login_required
def index(request):
    items = Items.objects.filter(created_by = request.user)

    return render(request, 'deshboard/index.html',{'items':items})
