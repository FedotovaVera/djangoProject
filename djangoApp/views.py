from django.shortcuts import render
from .models import Profile

def hello(request):
    return render(request, 'hello.html')


