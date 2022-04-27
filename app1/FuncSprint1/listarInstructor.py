from django.http import request
from django.shortcuts import render
from app1.models import Instructores
from django.http.response import HttpResponse


def listaInstructores(request):
    template = "listarInstructor.html"
    listaFormulario = ["Nombre","Apellido","NumeroDocumento"]
    diccionarioValores = dict()
    for e in listaFormulario:
        if not request.GET[e]:
            pass
        else:
            diccionarioValores[e] = request.GET[e]
    instructores = Instructores.objects.filter(Nombre = diccionarioValores["Nombre"])
    return render(request, template, {'instructores': instructores,
    'diccionario': diccionarioValores})

    #  nombre = request.GET["Nombre"] 
    #  if nombre:
    #      instructores = Instructores.objects.filter(Nombre = nombre)   
    #      return render(request, template, {'instructores':instructores}) 
    #  else:
    #      return HttpResponse('error')


