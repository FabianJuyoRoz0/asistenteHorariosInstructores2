from pickle import GET
from django.http import request
from django.shortcuts import render
from app1.models import Instructores, Contratacion
import csv, io
from django.contrib import messages
from datetime import date, datetime


def cargarBDinicial(request):
    template = "CargarBD.html"
    prompt = 'Ingrese el archivo .csv'
    render(request, template, {'prompt':prompt}) 
    #Validacion
    if request.method=="POST":
        prompt="El archivo no era de extension .csv o tenia diferente estructura"
        csv_file = request.FILES['file']
        if csv_file.name.endswith('.csv'):
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            for row in csv.reader(io_string, delimiter=',', quotechar="|"):
                if 'Nombre' in row[0] and 'Apellido' in row[1] and 'Tipo de documento' in row[2] and 'Numero de identificacion' in row[3] and 'Fecha Inicio' in row[4] and 'Fecha Fin' in row[5] and 'Supervisor' in row[6] and 'Horas mensuales' in row[7] and 'Correo electrónico' in row[8] and 'Número celular' in row[9]:
                    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                        try:
                            registro1=Instructores(
                                Nombre = column[0],
                                Apellido = column[1],
                                TipoDocumento = column[2],
                                NumeroDocumento = column[3],
                                correoElectronico = column[8],
                                numeroCelular = column[9],
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

