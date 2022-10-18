# import re
# from django.http import request
# from django.shortcuts import render
# from app1.models import Instructores
# from django.http.response import HttpResponse


# def listaInstructores(request):
#     template = "listarInstructor.html"
#     if c:=request.GET["Nombre"]:
#         qNombre = Instructores.objects.filter(Nombre = c)
#     else:
#         qNombre = Instructores.objects.all()
#     if c:=request.GET["Apellido"]:
#         qApellido = qNombre.filter(Apellido = c)
#     else:
#         qApellido = qNombre.all()
#     if c:=request.GET["NumeroDocumento"]:
#         qNumeroDocumento = qApellido.filter(NumeroDocumento = c)
#     else:
#         qNumeroDocumento = qApellido.all()
#     if c:=request.GET["TipoDocumento"]:
#         qTipoDocumento = qNumeroDocumento.filter(TipoDocumento = c)
#     else:
#         qTipoDocumento = qNumeroDocumento.all()
#     if c:=request.GET["numeroCelular"]:
#         qnumeroCelular = qTipoDocumento.filter(numeroCelular = c)
#     else:
#         qnumeroCelular = qTipoDocumento.all()
    
       
#     return render(request, template, {'instructores': qnumeroCelular})


