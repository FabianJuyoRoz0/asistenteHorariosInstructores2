import os
from django.http import HttpResponse, request
from django.shortcuts import render
from app1.models import Instructores

def alertayfinalizacion(request):
    if request.method == 'GET':
        lista=list(Instructores.objects.all().values_list('pk','horasMensualFormacion'))
        listainstructoresplanta=[]
        listainstructores=[]  
        for horas in lista:
            id=horas[0]
            cantidadhorainstructor=horas[1]
            if cantidadhorainstructor>=180:
                nombre=Instructores.objects.filter(id=id).values('Nombre')[0]['Nombre']
                apellido=Instructores.objects.filter(id=id).values('Apellido')[0]['Apellido']
                numeroidentificacion=Instructores.objects.filter(id=id).values('NumeroDocumento')[0]['NumeroDocumento']
                tipocontrato=Instructores.objects.filter(id=id).values('TipoDeContrato')[0]['TipoDeContrato']
                if tipocontrato==True:           
                    listainstructoresplanta.extend((nombre,apellido,numeroidentificacion))
                              
            elif cantidadhorainstructor>=152:
                nombre=Instructores.objects.filter(id=id).values('Nombre')[0]['Nombre']
                apellido=Instructores.objects.filter(id=id).values('Apellido')[0]['Apellido']
                numeroidentificacion=Instructores.objects.filter(id=id).values('NumeroDocumento')[0]['NumeroDocumento']
                tipocontrato=Instructores.objects.filter(id=id).values('TipoDeContrato')[0]['TipoDeContrato']
                if tipocontrato==False:           
                    listainstructores.extend((nombre,apellido,numeroidentificacion))
                    
        print("Estos son los de planta con sobrecarga "+str(listainstructoresplanta))
        print("Estos son los de contrato con sobrecarga "+str(listainstructores))



    template = "AlertasFinalizacion.html"   
    return render(request, template) 