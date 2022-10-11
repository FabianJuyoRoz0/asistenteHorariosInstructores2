from pickle import GET
<<<<<<< HEAD
from django.db import IntegrityError
=======
>>>>>>> 8152977f0a761e9c3ec2c8cbb16a4849b89c8233
from django.http import request
from django.shortcuts import get_object_or_404, render
from app1.models import Instructores
import csv, io
from django.contrib import messages
from datetime import date, datetime


def cargarBDinicial(request):
    template = "CargarBD.html"
<<<<<<< HEAD
    aviso=[]
    prompt = 'Ingrese el archivo .csv'
    prompt2= 'Instructores repetidos: '
=======
    prompt = 'Ingrese el archivo .csv'
>>>>>>> 8152977f0a761e9c3ec2c8cbb16a4849b89c8233
    render(request, template, {'prompt':prompt}) 
    #Validacion
    if request.method=="POST":
        prompt="El archivo no era de extension .csv o tenia diferente estructura"
<<<<<<< HEAD
        prompt2="Instructores repetidos: "
=======
>>>>>>> 8152977f0a761e9c3ec2c8cbb16a4849b89c8233
        csv_file = request.FILES['file']
        if csv_file.name.endswith('.csv'):
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            for row in csv.reader(io_string, delimiter=',', quotechar="|"):
<<<<<<< HEAD
                if 'Nombre' in row[0] and 'Apellido' in row[1] and 'Tipo de documento' in row[2] and 'Numero de identificacion' in row[3] and 'Fecha Inicio' in row[4] and 'Fecha Fin' in row[5] and 'Supervisor' in row[6] and 'Horas mensuales' in row[7] and 'Correo electrónico' in row[8] and 'Número celular' in row[9] and 'Tipo Contrato' in row[10]:
                    prompt="El archivo csv se cargo exitosamente" 
=======
                if 'Nombre' in row[0] and 'Apellido' in row[1] and 'Tipo de documento' in row[2] and 'Numero de identificacion' in row[3] and 'Fecha Inicio' in row[4] and 'Fecha Fin' in row[5] and 'Supervisor' in row[6] and 'Horas mensuales' in row[7] and 'Correo electrónico' in row[8] and 'Número celular' in row[9]:
>>>>>>> 8152977f0a761e9c3ec2c8cbb16a4849b89c8233
                    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                        try:
                            registro1=Instructores(
                                Nombre = column[0],
                                Apellido = column[1],
                                TipoDocumento = column[2],
                                NumeroDocumento = column[3],
                                correoElectronico = column[8],
                                numeroCelular = column[9],
<<<<<<< HEAD
                                Fecha_Inicio = datetime.strptime(column[4], '%Y-%m-%d'),
                                Fecha_Fin = datetime.strptime(column[5], '%Y-%m-%d'),
                                supervisora = column[6],
                                horasMensualFormacion = column[7],
                                TipoDeContrato= column[10]
                                )
                            validacion=[column[0],column[1],column[3]]
                            registro1.save()
                        #En caso de que hayan registros repetidos
                        except IntegrityError:
                            aviso.append((validacion))
                            prompt='Registros guardados, algunos registros ya existian y fueron evitados:' + str(aviso)
                            continue
                        #En caso de que la plantilla cuente con un solo registro
                        except IndexError:
                            prompt='Intente que la plantilla tenga mas de 1 registro'
                            continue

                                 
                                                             
                    return render(request, template, {'prompt':prompt})


   


    return render(request, template, {"prompt":prompt})

    
def listaInstructores(request):
    template='listarInstructor.html'
    instructores=Instructores.objects.all()

    return render(request, template, {"instructores" : instructores})



# def editarInstructor(request, id):
#     template='listarInstructor.html'
#     if request.method == 'POST':
        


    

#     return render(request,template)
    
=======
                                )
                            registro1.save()
                            
                            
                            Contratacion.objects.create(
                            Fecha_Inicio = datetime.strptime(column[4], '%Y-%m-%d'),
                            Fecha_Fin = datetime.strptime(column[5], '%Y-%m-%d'),
                            supervisora = column[6],
                            id_Instructor = Instructores.objects.filter(NumeroDocumento = column[3])[0],
                            horasMensualFormacion = column[7]
                                 )
                        except:
                            continue
                                            
                    prompt="El archivo csv se cargo exitosamente"               
                    return render(request, template, {'prompt':prompt})


   


    return render(request, template, {"prompt":prompt})

def editarInstructor(request):
    pass
    

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

>>>>>>> 8152977f0a761e9c3ec2c8cbb16a4849b89c8233
