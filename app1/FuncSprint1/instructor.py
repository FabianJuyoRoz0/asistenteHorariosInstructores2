from django.http import request
from django.shortcuts import render
from app1.models import Instructores, Contratacion
import csv, io
from django.contrib import messages
from datetime import date, datetime


def cargarBDinicial(request):
    template = "CargarBD.html"
    prompt = {'order': 'El orden del archivo .csv debe ser nombre, apellido, número de documento, fecha de inicio contrato, fecha fin contrato, supervisor (a), horas mensuales para impartir formación, correo electrónico, teléfono, profesión'}
    render(request, template) 
    if request.method == "GET":
        return render(request, template)
    ctx = {}
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        Instructores.objects.update_or_create(
            Nombre = column[0],
            Apellido = column[1],
            TipoDocumento = column[2],
            NumeroDocumento = column[3],
            correoElectronico = column[8],
            numeroCelular = column[9],
            )
        Contratacion.objects.update_or_create(
            Fecha_Inicio = datetime.strptime(column[4], '%Y-%m-%d'),
            Fecha_Fin = datetime.strptime(column[5], '%Y-%m-%d'),
            supervisora = column[6],
            id_Instructor = Instructores.objects.filter(NumeroDocumento = column[3])[0],
            horasMensualFormacion = column[7]
            )
        return render(request, template) 

def editarInstructor(request):
    template = "editarInstructor.html"
##    instructor = Instructores.objects.filter(id=id_Instructor).first()
        
    return render(request, template)