from django.http import request
from django.shortcuts import render

def inicioSesion(request):
    template = "inicioSesion.html"   
    return render(request, template) 
