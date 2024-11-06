from django.shortcuts import render, redirect
from . import models


# Create your views here.
def index(request):
    context = {
        'users' : models.get_all_users()
    }
    return render(request, "index.html" , context)

def add(request):
    models.insert_to_users(request.POST)
    return redirect('/')

def remove(request, id):
    models.delete_from_users(id)
    return redirect('/')
