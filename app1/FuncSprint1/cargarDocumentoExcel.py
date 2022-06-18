from django.http import request
from django.shortcuts import render

def cargarExcel(request):
    template = "cargarXMLS.html"   
    return render(request, template) 


