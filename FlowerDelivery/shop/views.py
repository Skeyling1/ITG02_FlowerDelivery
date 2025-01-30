from django.shortcuts import render
from .models import Good, Order


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def registration(request):
    return render(request, 'shop/registration.html')


def cabinet(request):
    goods = Good.objects.all()
    orders = Order.objects.all()
    return render(request, 'shop/cabinet.html', {'goods': goods, 'orders': orders})