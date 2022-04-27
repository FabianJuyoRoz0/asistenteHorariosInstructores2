# # Insumos: Base de datos con información en las siguientes tablas:
# #   Fichas de caracterización       Instructores            Ambientes   ProgramasFormacion
# #   Competencias                    Resultados              Orden RAP 
# #   Coordinaciones 
# # Criterios:    
# #   a) Los instructores y ambientes asignados a una coordinación deben atender a        los        programas de dicha coordinación 
# #   b) Los eventos son una concatenación de la competecia de aprendizaje + el resultado de aprendizaje + "actividad de aprendizaje"
# #   c) La duración del evento no debe sobrepasar la jornada de la ficha
# #   d) Tener en cuenta la modalidad de la formación
# #   e) El instructor no debe sobrepasar las 10 horas diarias, ni semanalmente de la cantidad de horas / 4
# # Salidas:
# #   Eventos en la tabla Horario_Instructores
# from datetime import date, datetime, timedelta
# from asistenteHorarios.models import FichasCaracterizacion, Resultados
# # Algoritmo
# # 1. Determinar las necesidades de formación
# #   1.1. Obtener las fichas activas (son en las que no se ha cumplido su fecha de etapa lectiva)
# def sena15():
#     fechaActual = datetime.now().date()
#     FichasActivas = FichasCaracterizacion.objects.filter(FechaFinEtapaLectiva__gte = fechaActual)
#     result = Resultados.objects.all()
#     resp = set(result) - set(FichasActivas[0].Avance.all())
#     return resp
# #   1.2. Determinar los RAP's que no estan abordados (consultar la tabla Resultados)

# #   1.3. Los RAP's no abordados deben programarse de acuerdo al orden establecido en la tabla OrdenRAP
# #Competencias.objects.get(id = consultaRapNoAbordados[0].Competencia.id).competencia
# # 2. Revisar que instructor (a) puede atender dicha necesidad
# #   2.1. Obtener la lista de instructores disponibles de acuerdo al perfil, con disponibilidad de horario
# # 3. Hacer la programación
# #   3.1. Realizar la salida