from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Good, Order


# Create your views here.

def index(request):
    goods = Good.objects.all()
    username = request.user.username
    if request.method == 'POST':
        user_base = request.POST['username']
        goods_base = request.POST['good_title']
        new_order = Order(user=user_base, goods=goods_base)
        new_order.save()
    return render(request, 'shop/index.html', {'goods': goods, 'username': username})


def registration(request):
    return render(request, 'shop/registration.html')


@login_required
def cabinet(request):
    orders = Order.objects.all()
    username = request.user.username
    return render(request, 'shop/cabinet.html', {'orders': orders, 'username': username})