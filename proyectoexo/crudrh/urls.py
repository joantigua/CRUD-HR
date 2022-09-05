from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('competencias/', views.competencias),
    path('create_competencias/', views.createCompetencias),
    path('idiomas/', views.idiomas),
    path('create_idiomas/', views.createIdiomas),
    path('capacitaciones/', views.capacitaciones),
    path('create_capacitaciones/', views.createCapacitaciones),
    path('puestos/', views.puestos),
    path('create_puestos/', views.createPuestos),
    path('experiencia_laboral/', views.experiencia_laboral),
    path('create_experiencia_laboral/', views.createExperiencia_laboral),
    path('empleados/', views.empleados),
    path('create_empleados/', views.createEmpleados),
    path('candidatos/', views.candidatos),
    path('create_candidatos/', views.createCandidatos),
    path('login/', views.loginPage),
    path('', views.loginPage),
    path('register/', views.registerPage),
    path('logout/', views.logoutUser),
    path('user/', views.userPage),
]
