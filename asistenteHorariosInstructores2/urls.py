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
from app1.FuncSprint1 import inicioSesion, instructor,Sena11,cargarFichas,cargarSemaforo,cargarProgramasFormacion, HorasInstructor,alertaFinalizacion

urlpatterns = [
    path('inicio/', inicioSesion.inicioSesion),
    path('admin/', admin.site.urls),
    path('CargarBDinicial/', instructor.cargarBDinicial),
    path('BuscarInstructor/', instructor.buscarInstructores),
    path('ListarInstructor/', instructor.listaInstructores),
    path('ListarFichas/', instructor.listaFichas),
    path('EditarFicha/<int:id>', instructor.editarFicha, name='editarficha'),
    path('EliminarFicha/<int:id>', instructor.eliminarFicha, name='eliminarficha'),
    path('EditarInstructor/<int:id>', instructor.editarInstructor, name='editarinstructor'),
    path('EliminarInstructor/<int:id>', instructor.eliminarInstructor, name='eliminarinstructor'),
    path('CargarFichas/', cargarFichas.cargarFichasBD),
    path('CargarSemaforo/', cargarSemaforo.cargarSemaforoBD),
    path('CargarProgramas/', cargarProgramasFormacion.cargarProgramasBD),
    path('HorasInstructor/', HorasInstructor.obtenerHoras),
    path('AlertaFinalizacion/', alertaFinalizacion.alertayfinalizacion),
    path('ProgresoFicha/', cargarFichas.progresoficha)
]
