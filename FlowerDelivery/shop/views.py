from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
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
        return redirect('new_order')
    return render(request, 'shop/index.html', {'goods': goods, 'username': username})


@login_required
def new_order(request):
    orders = Order.objects.filter(user=request.user.username)
    order = orders.last()
    username = request.user.username
    return render(request, 'shop/new_order.html', {'order': order, 'username': username})

def del_new_order(request):
    orders = Order.objects.filter(user=request.user.username)
    order = orders.last()
    order.delete()
    return redirect('home')


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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)  # Выход из системы
    return redirect('home')  # Перенаправление на главную страницу или другую страницу


@login_required
def cabinet(request):
    orders = Order.objects.filter(user=request.user.username)
    username = request.user.username
    return render(request, 'shop/cabinet.html', {'orders': orders, 'username': username})


