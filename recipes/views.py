from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Daniel Neves',
    })

def contato(request):
    return render(request, 'me-apague/temp.html')

def sobre(request):
    return HttpResponse('Sobre')

# Create your views here.
