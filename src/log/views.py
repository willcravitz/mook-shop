from django.shortcuts import render    
from django.http import HttpResponse

def index(request):
    context = {"welcome": "Hello, world!"}

    return render(request, "log/index.html", context)