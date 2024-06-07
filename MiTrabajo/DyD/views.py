from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'DyD/index.html', context)


def login(request):
    context = {}
    return render(request, 'DyD/login.html', context)


def inicio(request):
    context = {}
    return render(request, 'DyD/inicio.html', context)


def recursos(request):
    context = {}
    return render(request, 'DyD/Recursos.html', context)


def inventario(request):
    context = {}
    return render(request, 'DyD/Inventario.html', context)
