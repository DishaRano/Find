from django.shortcuts import render, redirect
from .models import Item

from django.views.generic import ListView
from django.db.models import Q
def home(request):
   return render(request, 'home.html')

def video(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        obj = Item.objects.all().filter(name__icontains=query)
        return render(request, 'video.html', {'obj': obj})

