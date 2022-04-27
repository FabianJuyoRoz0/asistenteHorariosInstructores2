# #Obtener la cantidad de horas cargadas de cada instructor y compararla con la cantidad de horas que debería impartir, dependiendo de un periodo determinado de tiempo

# # Obtener el objeto (registro del instructor) - consulta con filtro para un instructor determinado
# # 1. Consultar la BD y obtener las horas mensuales que debe impartir un instructor, de la tabla Contratación
# #2. Constultar la BD y obtener las horas programadas a un instructor a partir de los eventos de la tabla Horario_Instructor. QuerySet
# #3. Realizar algoritmo para obtener la sumatoria de la duración de los eventos
# #4. Realizar la comparación

# from asistenteHorarios.models import Horario_Instructor, Instructores, Contratacion
# from datetime import datetime, timedelta

# def sena10(instructor, fechaInicio, fechaFin):
#     consultaHorarioInstructor = Horario_Instructor.objects.filter(id_Instructor = instructor[0], Fecha_Inicio__gte = fechaInicio).filter(Fecha_Fin__lte = fechaFin)
#     dur = timedelta(0)
#     consultaHoras=Contratacion.objects.get(id_Instructor=instructor[0])
#     horasMensualFormacion=consultaHoras.horasMensualFormacion
#     # Horas_mes=timedelta(seconds=horasMensualFormacion)
#     periodo=fechaFin-fechaInicio
#     p=periodo.total_seconds()/2592000
#     for iteracion in consultaHorarioInstructor:
#         dur += iteracion.Fecha_Fin - iteracion.Fecha_Inicio
#     d=dur.total_seconds()/3600
#     r=horasMensualFormacion*p       # cantidad de horas que debe dar formación el instructor
#     r1=timedelta(seconds=r*3600)
#     diferencia=d-r
#     return dur,diferencia,p

# #instructor = Instructores.objects.filter(id = 6) 
# # consultaHorasMensualFormacion = Contratacion.objects.filter(id_Instructor = instructor[0]) 
# # HorasMensualFormacion = consultaHorasMensualFormacion[0].horasMensualFormacion

# # PeriodoTiempo = 1             # suponiendo meses el inicio como la fecha de inicio 

# #print(sena10(instructor,PeriodoTiempo,HorasMensualFormacion))

# # Función hipotetica para hacer la prueba
# class sena10Prueba:
#     def __init__(self, id):
#         self.id = id
#     #     self.desviacion = desviacion

#     def instructor(self):
#         return Instructores.objects.get(id = self)

#     def instructorFalla(self):
#         return None