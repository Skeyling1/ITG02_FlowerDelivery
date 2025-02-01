from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm, CustomerNotesForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Good, Order
import requests


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
    if request.method == 'POST':
        form = CustomerNotesForm(request.POST)
        if form.is_valid():
            #отпрвавляем в ЧАТ имя, товар, коммент, картинку
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





def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Сообщение отправлено успешно!")
    else:
        print("Ошибка при отправке сообщения:", response.text)


if __name__ == "__main__":
    bot_token = "YOUR_BOT_TOKEN"  # Замените на ваш токен
    chat_id = "YOUR_CHAT_ID"  # Замените на ваш chat_id
    message = "Привет, это сообщение из Python!"

    send_message(bot_token, chat_id, message)