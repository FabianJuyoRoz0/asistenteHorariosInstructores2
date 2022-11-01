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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app1 import views
from app1.FuncSprint1 import inicioSesion, instructor,cargarInstructorUnico,listarInstructor,Sena11,cargarFichas,cargarSemaforo,cargarProgramasFormacion, HorasInstructor,alertaFinalizacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_user', views.login_user, name='login_user'),
    path('login/', auth_views.LoginView.as_view(template_name="iniciosesion.html"), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('CargarBDinicial/', views.cargarBDInicial, name='app1'),
    path('CargarInstructor/', cargarInstructorUnico.cargarInstructor),
    path('ListarInstructor/', listarInstructor.listaInstructores),
    path('EditarInstructor/', instructor.instructorPrueba.editarInstructor, name='editarInstructor'),
    path('CargarFichas/', cargarFichas.cargarFichasBD),
    path('CargarSemaforo/', views.cargarSemaforo, name="cargarSemaforo"),
    path('CargarProgramas/', cargarProgramasFormacion.cargarProgramasBD),
    path('HorasInstructor/', HorasInstructor.consultaHoras),
    path('AlertaFinalizacion/', alertaFinalizacion.alertayfinalizacion)
]
