from django.http import request
from django.shortcuts import render

def cargarInstructor(request):
    template = "cargarInstructor.html"   
    return render(request, template) 


