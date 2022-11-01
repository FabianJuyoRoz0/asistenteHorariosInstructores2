from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login_user(request):
    return redirect('/login')

def logout_user(request):
    auth.logout(request)
    return redirect('/login')

def home(request):
    return render(request, 'home.html')

def cargarBDInicial(request):
    return render(request, 'cargarBD.html')

def cargarSemaforo(request):
    return render(request, 'cargarSemaforo.html')
