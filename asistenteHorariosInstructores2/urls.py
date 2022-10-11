"""asistenteHorariosInstructores2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.FuncSprint1 import inicioSesion, instructor,cargarInstructorUnico,Sena11,cargarFichas,cargarSemaforo,cargarProgramasFormacion, HorasInstructor,alertaFinalizacion

urlpatterns = [
    path('inicio/', inicioSesion.inicioSesion),
    path('admin/', admin.site.urls),
    path('CargarBDinicial/', instructor.cargarBDinicial),
    path('CargarInstructor/', cargarInstructorUnico.cargarInstructor),
    path('ListarInstructor/', instructor.listaInstructores),
    #path('EditarInstructor/<id>/', instructor.editarInstructor),
    path('CargarFichas/', cargarFichas.cargarFichasBD),
    path('CargarSemaforo/', cargarSemaforo.cargarSemaforoBD),
    path('CargarProgramas/', cargarProgramasFormacion.cargarProgramasBD),
    path('HorasInstructor/', HorasInstructor.obtenerHoras),
    path('AlertaFinalizacion/', alertaFinalizacion.alertayfinalizacion)
]
