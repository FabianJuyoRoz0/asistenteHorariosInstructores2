from django.http import request
from django.shortcuts import render
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from app1.models import fichasCaracterizacion

def cargarFichasBD(request):
    template="cargarFichas.html"
    fechaActual = datetime.today()
    TiempoParaRestar = timedelta(days=180)
    prompt = 'Ingrese el archivo .xml'

    if request.method=="POST":
        prompt="El archivo no era de extension .xml"
        xml= request.FILES['file']
        try:
            if xml.name.endswith('.xml'):
                xml_1=ET.parse(xml)
                raiz = xml_1.getroot()
                for dato in range (6,len(raiz[3][0])):    
                    fichas=raiz[3][0][dato][4][0].text
                    Jornadas= raiz[3][0][dato][10][0].text
                    Cantidad= raiz[3][0][dato][41][0].text
                    FechaInicioEtapaLectivas= datetime.strptime(raiz[3][0][dato][12][0].text, '%d/%m/%Y')
                    FechaFinFicha= datetime.strptime(raiz[3][0][dato][13][0].text, '%d/%m/%Y')
                    finalizacionEtapaLectiva = FechaFinFicha - TiempoParaRestar
        
                    if finalizacionEtapaLectiva > fechaActual:
                        registro1=fichasCaracterizacion(ficha=fichas,
                        Jornada=Jornadas,
                        CantidadAprendices=Cantidad,
                        FechaInicioEtapaLectiva=FechaInicioEtapaLectivas,
                        FechaFinEtapaLectiva=FechaFinFicha)
                        registro1.save()
                prompt="El archivo xml se cargo exitosamente"
                return render(request, template, {'prompt':prompt})    
        except:
            prompt="El archivo contiene fichas que ya estan en el registro"
            return render(request, template,{'prompt':prompt})
    return render(request, template,{'prompt':prompt})
    
    