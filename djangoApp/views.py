from django.shortcuts import render
from models import Example

def hello(request):
    context = {'var' : 'value'}
    return render(request, 'hello.html', context)

def main(request):
    ex = Example()
    ex.smth = 100
    ex.smth2 = 'something'
    ex.save()
    return render(request, 'main.html')

