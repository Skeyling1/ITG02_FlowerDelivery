from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def registration(request):
    return render(request, 'shop/registration.html')


def cabinet(request):
    return render(request, 'shop/cabinet.html')