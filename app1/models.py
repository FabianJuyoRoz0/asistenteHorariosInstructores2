from django.db import models

class Catalogo_Perfiles(models.Model):
    Perfil = models.CharField(max_length=30)

class Instructores(models.Model):
    NumeroDocumento = models.CharField(max_length=20, unique=True)
    TipoDocumento = models.CharField(max_length=2)  
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    id_Perfiles = models.ForeignKey(Catalogo_Perfiles, null=True, on_delete=models.CASCADE)
    correoElectronico = models.EmailField(max_length = 254)
    numeroCelular = models.CharField(max_length=10)
    Fecha_Inicio = models.DateField(null=True)
    Fecha_Fin = models.DateField(null=True)
    horasMensualFormacion = models.IntegerField(null=True)
    supervisora = models.CharField(max_length=50, null=True)
    TipoDeContrato= models.BooleanField(null=True)
    
    

class fichasCaracterizacion(models.Model):
    ficha= models.CharField(max_length=10, unique=True)
    FechaInicioEtapaLectiva= models.DateField()
    FechaFinEtapaLectiva= models.DateField()
    Jornada= models.CharField(max_length=10)
    CantidadAprendices= models.IntegerField()