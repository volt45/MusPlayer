from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

from player.models import User


def index(request):
    return render(request, 'player/templates/index.html')


def login(request):
    if request.method == 'POST':
        form = User(request.POST)
        logins = request.POST.get('login')
        password = request.POST.get('password')
        if not User.objects.filter(username=logins).exists():
            messages.error(request, 'Неверный логин или пароль')
            return redirect('/login')
    user = authenticate(request, username=logins, password=password)
    if user is not None:
        messages.success(request, 'Неверный логин или пароль')
        return redirect('/login')
    else:
        login(request, user)
        redirect('/index')
    return render(request, 'player/templates/login.html')


def registration(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('login')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dateBirth = request.POST.get('dateBirth')

        user = User.objects.filter(login=username)

        if user.exists():
            messages.info(request, "Такой пользователь уже существует")
            return redirect('/registration')
        user = User.objects.create_user(
            firstName=firstName,
            lastName=lastName,
            login=username,
            phone=phone,
            email=email,
            dateBirth=dateBirth,
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Пользователь создан успешно!")
        return redirect('/registration')
    return render(request, 'player/templates/registration.html')
