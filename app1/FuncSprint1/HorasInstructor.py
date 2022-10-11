from django.http import request
from django.shortcuts import render
from app1.models import Instructores


def obtenerHoras(request):
    template = "horasInstructor.html"
    if request.method == 'POST':
        try:
            documentoIngresado=(request.POST['text'])
            documentoIngresado= int(documentoIngresado)
            print("El request es POST")
            print(type(documentoIngresado))
            if Instructores.objects.filter(NumeroDocumento=documentoIngresado).exists():
                id= Instructores.objects.filter(NumeroDocumento=documentoIngresado).values('id')[0]['id']
                horas=Instructores.objects.filter(id=id).values('horasMensualFormacion')[0]['horasMensualFormacion']
                nombre=Instructores.objects.filter(id=id).values('Nombre')[0]['Nombre']
                apellido=Instructores.objects.filter(id=id).values('Apellido')[0]['Apellido']
                print(nombre)
                print(apellido)
                prompt="El instructor "+nombre + " "+apellido +" tiene " + str(horas) + " horas."
                return render(request, template, {'prompt':prompt})
            else:
                prompt="El instructor no esta registrado." 
                return render(request, template, {'prompt':prompt})
        except:
                prompt="Hubo un problema, ingrese unicamente numeros, sin espacios."
                return render(request, template, {'prompt':prompt})


    




    return render(request, template)

