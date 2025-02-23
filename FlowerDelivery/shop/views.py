from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm, CustomerNotesForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Good, Order
from .config import TOKEN, CHAT_ID
import asyncio
import os
from aiogram import Bot
from aiogram.types import FSInputFile

TOKEN = TOKEN
CHAT_ID = CHAT_ID



# Create your views here.

def index(request):
    goods = None
    if Good.objects.exists() == False:
        Good(good_title='Ромашки', price='857,97 ₽', picture='shop/img/1.jpg').save()
        Good(good_title='Белые розы', price='4461,45 ₽', picture='shop/img/2.jpg').save()
        Good(good_title='Букет Мини', price='3203,09 ₽', picture='shop/img/3.jpg').save()
        Good(good_title='Астры', price='2001,93 ₽', picture='shop/img/4.jpg').save()
        Good(good_title='Букет Ассорти', price='2608,23 ₽', picture='shop/img/5.jpg').save()
        Good(good_title='Оранжевые розы', price='3225,97 ₽', picture='shop/img/6.jpg').save()
        Good(good_title='Красные розы', price='3809,39 ₽', picture='shop/img/7.jpg').save()
        Good(good_title='Розовые розы', price='3088,69 ₽', picture='shop/img/8.jpg').save()
        Good(good_title='Пионы', price='2505,27 ₽', picture='shop/img/9.jpg').save()
    else:
        goods = Good.objects.all()
        username = request.user.username
        if request.user.is_authenticated:
            user = True
        else:
            user = None
        if request.method == 'POST':
            if request.user.is_authenticated:
                user_base = request.POST['username']
                goods_base = request.POST['good_title']
                picture_base = request.POST['picture']
                new_order = Order(user=user_base, goods=goods_base, picture=picture_base)
                new_order.save()
                return redirect('new_order')
            else:
                return redirect('login')
    return render(request, 'shop/index.html', {'goods': goods, 'username': username, 'user': user})



@login_required
def new_order(request):
    orders = Order.objects.filter(user=request.user.username)
    order = orders.last()
    username = request.user.username
    if request.method == 'POST':
        form = CustomerNotesForm(request.POST)
        if form.is_valid():
            message = (f"Зарегестрирован новый заказ от: {request.user.username} \n"
                       f"{order.goods} \n"
                       f"Комментарий: {form.cleaned_data['comment']}")
            asyncio.run(send_message(message, f"shop/static/{order.picture}"))
            return redirect('home')
    else:
        form = CustomerNotesForm()
    return render(request, 'shop/new_order.html', {'order': order, 'username': username, 'form': form})

def del_new_order(request):
    orders = Order.objects.filter(user=request.user.username)
    order = orders.last()
    order.delete()
    return redirect('home')


def approve_new_order(request):

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



async def send_message(message, IMAGE_PATH):
    bot = Bot(token=TOKEN)
    photo = FSInputFile(IMAGE_PATH)
    await bot.send_photo(chat_id=CHAT_ID, photo=photo)
    await bot.send_message(chat_id=CHAT_ID, text=message)
