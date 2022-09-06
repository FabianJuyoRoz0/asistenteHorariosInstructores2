from django.http import request
from django.shortcuts import render

def consultaHoras(request):
    template = "horasInstructor.html"   
    return render(request, template) 