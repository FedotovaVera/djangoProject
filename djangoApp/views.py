from django.shortcuts import render
from models import Users
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

def hello(request):
    t = Users.object.All()
    return render(request, 'hello.html')

