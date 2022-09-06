from django.http import request
from django.shortcuts import render

def cargarProgramasBD(request):
    template = "cargarProgramas.html"   
    return render(request, template) 