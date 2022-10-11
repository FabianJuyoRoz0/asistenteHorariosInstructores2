from django.http import request
from django.shortcuts import render
<<<<<<< HEAD
from app1.models import Instructores

=======
from app1.models import Contratacion,Instructores
>>>>>>> 8152977f0a761e9c3ec2c8cbb16a4849b89c8233

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
<<<<<<< HEAD
                horas=Instructores.objects.filter(id=id).values('horasMensualFormacion')[0]['horasMensualFormacion']
=======
                horas=Contratacion.objects.filter(id_Instructor_id=id).values('horasMensualFormacion')[0]['horasMensualFormacion']
>>>>>>> 8152977f0a761e9c3ec2c8cbb16a4849b89c8233
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

