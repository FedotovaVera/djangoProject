from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html')

def main(request):
    return render(request, 'main.html')
