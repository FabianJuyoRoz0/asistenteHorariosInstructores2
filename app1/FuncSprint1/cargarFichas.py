from django.http import request
from django.shortcuts import render

def cargarFichasBD(request):
    template = "cargarFichas.html"   
    return render(request, template) 