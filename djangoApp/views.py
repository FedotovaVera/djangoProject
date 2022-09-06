from django.shortcuts import render

def hello(request):
    context = {'var' : 'value'}
    return render(request, 'hello.html', context)

def main(request):
    return render(request, 'main.html')
