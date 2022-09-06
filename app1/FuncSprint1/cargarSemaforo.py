from django.http import request
from django.shortcuts import render

def cargarSemaforoBD(request):
    template = "cargarSemaforo.html"   
    return render(request, template) 