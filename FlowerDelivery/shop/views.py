from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
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


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'shop/registration.html', {'form': form})



@login_required
def cabinet(request):
    orders = Order.objects.filter(user=request.user.username)
    username = request.user.username
    return render(request, 'shop/cabinet.html', {'orders': orders, 'username': username})