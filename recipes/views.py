from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home1(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Danilo Moreira',
    })

def home2(request):
    return HttpResponse("Teste /home2")

def contato(request):
    return render(request, 'recipes/home.html')

def sobre(request):
    return HttpResponse("Sobre")