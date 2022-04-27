# 1. Conseguir horario de cada instructor y Conseguir cuantas horas al mes debe impartir el instructor
#   Alternativa 1:Consultando la tabla Horario_Instructor "hasta cuando el instructor se queda sin eventos" y la  
#   Alternativa 2: Conseguir el querySet de la consulta  a la tabla Horario_Instructor, con los parametros de el instructor, el periodo de tiempo y horasMensualFormacion, y 
#   se analiza cuando termina cada uno de los RAP
#   "Cada vez que termine un RAP se genera un previsión"
#   Entregar al usuario el cuando (al menos un mes antes) y cuáles son los últiomos RAP's con los que el insructor termina
#   A través de un listado en orden del instructor que menos carga tenga la que mas tenga 
# -Ver cuantas horas utiliza a diario para una competencia
# -Realizar funcion que en base a las horas restantes y las horas utilizadas a diario
# prevea la finalizacion de una competencia
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

def HorararioHora(request):
    template = "HorarioYHoras.html"
    return render(request, template) 

# # ///////////////
# from datetime import date
# from asistenteHorarios.models import Horario_Instructor, Instructores

# class sena11:
#     ultima_fecha=date(2021,1,1)
#     PrevisionFechaFin = dict()
#     InstructorInoficioso = list()

#     #def ultimaFecha(self):
#     #   self.ultima_fecha=self.consultahorario()
   
#     @classmethod
#     def consultahorario(cls):
#         listaInstructores=Instructores.objects.all()       
        
#         for instructor in listaInstructores:
#            consulta = Horario_Instructor.objects.filter(id_Instructor = instructor).order_by("-Fecha_Fin")     
#            if consulta:
#                 cls.PrevisionFechaFin[instructor] = consulta[0].Fecha_Fin
#            else:
#                if instructor not in cls.InstructorInoficioso:
#                 cls.InstructorInoficioso.append(instructor)
#         return 
        
#     def prueba_imprimir():
#         print("Prueba impresion")

#     def consultahorario1():
#         consulta_instructor=Instructores.objects.get(id=6)
#         consulta=Horario_Instructor.objects.filter(id_Instructor=consulta_instructor).order_by("-Fecha_Fin")
#         fecha=consulta[0]
#         print("La ultima fecha es: ", fecha.Fecha_Fin)
#         return fecha



# # lista = list()
# # for fechaFin in listaInstructores:
# #      consulta = Horario_Instructor.objects.filter(id_Instructor = fechaFin).order_by("-Fecha_Fin")     
# #      if consulta:
# #        lista.append(consulta[0].Fecha_Fin)
# #        print(lista)

# # PrevisionFechaFin = dict()
# # InstructorInoficioso = list()
# # for fechaFin in listaInstructores
# #         consulta = Horario_Instructor.objects.filter(id_Instructor = fechaFin).order_by("-Fecha_Fin")     
# #         if consulta:
# #             PrevisionFechaFin[fechaFin] = consulta[0].Fecha_Fin
# #         else:
# #             InstructorInoficioso.append(fechaFin)
# # print(PrevisionFechaFin)