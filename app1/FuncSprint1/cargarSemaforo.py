from django.http import request
from django.shortcuts import render
from app1.models import semaforo
from django.contrib import messages
import csv, io

    
def cargarSemaforoData(request):
    template = "cargarSemaforo.html"

    render(request, template)
    
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        semaforo.objects.update_or_create(
            idCompetencias=column[0],
            NoRafs=column[1],
            HoraTotales=column[2],
            I=column[3],
            II=column[4],
            III=column[5],
            EP=column[6],
            HorasTrimestreI=column[7],
            HorasTrimestreII=column[8],
            HorasTrimestreIII=column[9],
            Total=column[10],
            TotalHoraCompetencia=column[11],
            ResultadoAprendizaje=column[12],
        )
        
        return render(request, template)
