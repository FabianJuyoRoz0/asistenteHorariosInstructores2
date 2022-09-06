from django.http import request
from django.shortcuts import render

def alertayfinalizacion(request):
    template = "AlertasFinalizacion.html"   
    return render(request, template) 