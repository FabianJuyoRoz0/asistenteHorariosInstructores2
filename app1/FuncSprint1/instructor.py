from pickle import GET
from django.db import IntegrityError
from django.http import request
from django.shortcuts import get_object_or_404, render
from app1.models import Instructores
import csv, io
from django.contrib import messages
from datetime import date, datetime


def cargarBDinicial(request):
    template = "CargarBD.html"
    aviso=[]
    prompt = 'Solo formato .csv admitido'
    prompt2= 'Instructores repetidos: '
    render(request, template, {'prompt':prompt}) 
    #Validacion
    if request.method=="POST":
        prompt="El archivo no era de extension .csv o tenia diferente estructura"
        prompt2="Instructores repetidos: "
        csv_file = request.FILES['file']
        if csv_file.name.endswith('.csv'):
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            for row in csv.reader(io_string, delimiter=',', quotechar="|"):
                if 'Nombre' in row[0] and 'Apellido' in row[1] and 'Tipo de documento' in row[2] and 'Numero de identificacion' in row[3] and 'Fecha Inicio' in row[4] and 'Fecha Fin' in row[5] and 'Supervisor' in row[6] and 'Horas mensuales' in row[7] and 'Correo electrónico' in row[8] and 'Número celular' in row[9] and 'Tipo Contrato' in row[10]:
                    prompt="El archivo csv se cargo exitosamente" 
                    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                        try:
                            registro1=Instructores(
                                Nombre = column[0],
                                Apellido = column[1],
                                TipoDocumento = column[2],
                                NumeroDocumento = column[3],
                                correoElectronico = column[8],
                                numeroCelular = column[9],
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
                            prompt='Utilice una plantilla con mas de un registro, el unico registro se guardo.'
                            continue
                            
                    
                                 
                                                             
                    return render(request, template, {'prompt':prompt})


   


    return render(request, template, {"prompt":prompt})

    
def listaInstructores(request):
    template='listarInstructor.html'
    instructores=Instructores.objects.all()
    contexto={"instructores" : instructores}
    return render(request, template, contexto)


def editarInstructor(request, id):
    instructor= Instructores.objects.get(id=id)
    template='editarInstructor.html'
    template2='listarInstructor.html'
    if request.method=="POST":
            nombre = request.POST.get('Nombre')
            apellido = request.POST.get('Apellido')
            numerodoc= request.POST.get('NumeroDocumento')
            tipodoc= request.POST.get('TipoDocumento')
            telefono= request.POST.get('numeroCelular')
            correo= request.POST.get('correoElectronico')
            fechainicio=request.POST.get('Fecha_Inicio')
            fechafin=request.POST.get('Fecha_Fin')
            supervisor=request.POST.get('supervisora')
            horasmensualformacion=request.POST.get('horasMensualFormacion')
            Instructores.objects.filter(id=id).update(
                    Nombre = nombre,
                    Apellido = apellido,
                    TipoDocumento = tipodoc,
                    NumeroDocumento = numerodoc,
                    correoElectronico = correo,
                    numeroCelular = telefono,
                    Fecha_Inicio = datetime.strptime(fechainicio, '%Y-%m-%d'),
                    Fecha_Fin = datetime.strptime(fechafin, '%Y-%m-%d'),
                    supervisora = supervisor,
                    horasMensualFormacion = horasmensualformacion)
            template2='listarInstructor.html'
            instructores=Instructores.objects.all()
            contexto={"instructores" : instructores}
            return render(request, template2, contexto)
    return render(request,template,{"instructor": instructor})


 
def eliminarInstructor(request,id):
    instructor= Instructores.objects.get(id=id)
    template='editarInstructor.html'
    template2='listarInstructor.html'
    if request.method=="GET":
            Instructores.objects.filter(id=id).delete()
            instructores=Instructores.objects.all()
            contexto={"instructores" : instructores}
            return render(request, template2, contexto)
    return render(request,template,{"instructor": instructor})



def buscarInstructores(request):
    template='buscarInstructor.html'

        
    return render(request,template)

 
