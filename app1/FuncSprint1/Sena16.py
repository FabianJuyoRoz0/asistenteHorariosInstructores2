# # 1.Obtener la cantidad de horas cargadas de cada instructor Anteriormente echa por un compañero
# # 2.Llamar la cantidad de horas del anterior punto
# # 3.Hacer una funcion 
# # 4.Una condicion adentro de la funcion llamando la cantidad de Horas 
# # 5.comparando la cantidad de horas resividas  con las horas que se necesita hacer
# # 6.sacar una arlerta dependiendo los reultados de las comparaciones

# #Mensualmente 171 horas de base 1 semana = 40, 8 horas diarias
# from asistenteHorarios.models import Horario_Instructor,Instructores,Contratacion
# # from asistenteHorarios.models.Contratacion import horasMensualFormacion
# from  asistenteHorarios.FuncSprint1.Sena10 import sena10

# #CargaAcademica_men=160
# # CargaAcademica_sem=40
# # CargaAcademica_dia=8

# # Horas= sena10(1)
# # Periodo= sena10(2)
# # margen=20

# def sena16(instructor, fechaInicio, fechaFin):
#     margen = 20
#     conSena10 = sena10(instructor, fechaInicio, fechaFin)
#     diferencia = conSena10[1]
#     if diferencia < -margen:
#         print("el instructor ", instructor.Nombre, 'tiene alarma por baja ejecución de horas', 'ya que en el periodo evaluado debió haber realizado ', 160*conSena10[2], 'pero solo realizó ', conSena10[0])
#     else:
#         if diferencia > margen:
#             print("el instructor se esta sobreejecutando")
#         else:
#             print('esta bien')
#     # Instructor = Horario_Instructor.objects.filter( instructor[0], fechaInicio).filter( fechaFin)
#     # margenPositivo=periodo + margen
#     # margenNegativo= -20

#     # # for Horas in Instructor:
#     # # Alerta por alta carga academica    
#     # if Horas > margenPositivo:
#     #         return render(f"Te has pasado de las horas de clase predefinidas llevas: {Horas} Horas de {margenPositivo} Horas de clase que debes hacer. ")
#     # # Alerta por baja carga academica   
#     # elif Horas < margenNegativo:
#     #         return render(f"Te faltan Horas de clase por hacer llevas: {Horas} Horas de {margenNegativo} Horas de clase que debes hacer.")
#     # # Alerta Horas perfectas
#     # elif Horas == CargaAcademica_men :
#     #         return render(f"Bien Tienes tus horas de clase completas Llevas: {Horas} Horas de {CargaAcademica_men} Horas completas 👍. ") 
#     # else:
#     #         return render(f"LLevas mensualmente {Horas} Horas de {CargaAcademica_men} Horas . ") 

# # return render (margen, Horas , periodo, CargaAcademica_men,margenNegativo,margenPositivo )