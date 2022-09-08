from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.generic import *

# Create your views here.
from .models import *
from .forms import *
from .decorators import *

@login_required(login_url= "http://127.0.0.1:8000/login")

def home(request):
    return render(request, 'crudrh/home_page.html')

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def competencias(request):
  competencias = Competencias.objects.all()
  return render(request, 'crudrh/competencias.html', {'competencias' : competencias})

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def createCompetencias(request):
  form = CompetenciasForm()
  context = { 'form':form }
  if request.method == 'POST':
    form = CompetenciasForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/competencias')
  return render(request, 'crudrh/competencias_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def updateCompetencias(request, id):
  competencias = Competencias.objects.get(pk = id)
  form = CompetenciasForm(request.POST or None, instance = competencias)
  if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/competencias')
  context = { 
    'form':form,
    'competencias':competencias,
  }
  return render(request, 'crudrh/competencias_form_update.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def deleteCompetencias(request, id):
  competencias = Competencias.objects.get(pk = id)
  competencias.delete()
  return redirect('http://127.0.0.1:8000/competencias')

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def idiomas(request):
  idiomas = Idiomas.objects.all()
  return render(request, 'crudrh/idiomas.html', {'idiomas' : idiomas})

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def createIdiomas(request):
  form = IdiomasForm()
  context = { 'form':form }
  if request.method == 'POST':
    form = IdiomasForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/idiomas')
  return render(request, 'crudrh/idiomas_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def updateIdiomas(request, id):
  idiomas = Idiomas.objects.get(pk = id)
  form = IdiomasForm(request.POST or None, instance = idiomas)
  if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/idiomas')
  context = { 
    'form':form,
    'idiomas':idiomas,
  }
  return render(request, 'crudrh/idiomas_form_update.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def deleteIdiomas(request):
  idiomas = Idiomas.objects.get(pk = id)
  idiomas.delete()
  return redirect('http://127.0.0.1:8000/idiomas')

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def capacitaciones(request):
  capacitaciones = Capacitaciones.objects.all()
  return render(request, 'crudrh/capacitaciones.html', {'capacitaciones' : capacitaciones})

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def createCapacitaciones(request):
  form = CapacitacionesForm()
  context = { 'form':form }
  if request.method == 'POST':
    form = CapacitacionesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/capacitaciones')
  return render(request, 'crudrh/capacitaciones_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def updateCapacitaciones(request, id):
  capacitaciones = Capacitaciones.objects.get(pk = id)
  form = CapacitacionesForm(request.POST or None, instance = capacitaciones)
  if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/capacitaciones')
  context = { 
    'form':form,
    'capacitaciones':capacitaciones,
  }
  return render(request, 'crudrh/capacitaciones_form_update.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def deleteCapacitaciones(request):
  capacitaciones = Capacitaciones.objects.get(pk = id)
  capacitaciones.delete()
  return redirect('http://127.0.0.1:8000/capacitaciones')


@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def puestos(request):
  puestos = Puestos.objects.all()
  return render(request, 'crudrh/puestos.html', {'puestos' : puestos})

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def createPuestos(request):
  form = PuestosForm()
  context = { 'form':form }
  if request.method == 'POST':
    form = PuestosForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/puestos')
  return render(request, 'crudrh/puestos_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def updatePuestos(request, id):
  puestos = Puestos.objects.get(pk = id)
  form = PuestosForm(request.POST or None, instance = puestos)
  if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/puestos')
  context = { 
    'form':form,
    'puestos':puestos,
  }
  return render(request, 'crudrh/puestos_form_update.html', context)


@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def deletePuestos(request):
  puestos = Puestos.objects.get(pk = id)
  puestos.delete()
  return redirect('http://127.0.0.1:8000/puestos')

@login_required(login_url= "http://127.0.0.1:8000/login")
def experiencia_laboral(request):
  experiencia_laboral = Experiencia_Laboral.objects.all()
  return render(request, 'crudrh/experiencia_laboral.html', {'experiencia_laboral' : experiencia_laboral})

@login_required(login_url= "http://127.0.0.1:8000/login")
def createExperienciaLaboral(request):
  form = Experiencia_LaboralForm()
  context = { 'form':form }
  if request.method == 'POST':
    form = Experiencia_LaboralForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/experiencia_laboral')
  return render(request, 'crudrh/experiencia_laboral_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
def updateExperienciaLaboral(request, id):
  experiencia_laboral = Experiencia_Laboral.objects.get(pk = id)
  form = Experiencia_LaboralForm(request.POST or None, instance = experiencia_laboral)
  if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/experiencia_laboral')
  context = { 
    'form':form,
    'experiencia_laboral':experiencia_laboral,
  }
  return render(request, 'crudrh/experiencia_laboral_form_update.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
def deleteExperienciaLaboral(request):
  experiencia_laboral = Experiencia_Laboral.objects.get(pk = id)
  experiencia_laboral.delete()
  return redirect('http://127.0.0.1:8000/experiencia_laboral')

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def empleados(request):
  empleados = Empleados.objects.all()
  return render(request, 'crudrh/empleados.html', {'empleados' : empleados})

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def createEmpleados(request):
  form = EmpleadosForm()
  context = { 'form':form }
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = EmpleadosForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/empleados')
  return render(request, 'crudrh/empleados_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def updateEmpleados(request, id):
  empleados = Empleados.objects.get(pk = id)
  form = EmpleadosForm(request.POST or None, instance = empleados)
  if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/empleados')
  context = { 
    'form':form,
    'empleados':empleados,
  }
  return render(request, 'crudrh/empleados_form_update.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['admin'])
def deleteEmpleados(request):
  empleados = Empleados.objects.get(pk = id)
  empleados.delete()
  return redirect('http://127.0.0.1:8000/empleados')

@login_required(login_url= "http://127.0.0.1:8000/login")
def candidatos(request):
  candidatos = Candidatos.objects.all()

  return render(request, 'crudrh/candidatos.html', {'candidatos' : candidatos})

@login_required(login_url= "http://127.0.0.1:8000/login")
def createCandidatos(request):
  form = CandidatosForm()
  context = { 'form':form }
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = CandidatosForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/candidatos')
  return render(request, 'crudrh/candidatos_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
def updateCandidatos(request, id):
  candidatos = Candidatos.objects.get(pk = id)
  form = CandidatosForm(request.POST or None, instance = candidatos)
  if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/candidatos')
  context = { 
    'form':form,
    'candidatos':candidatos,
  }
  return render(request, 'crudrh/candidatos_form_update.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
def deleteCandidatos(request):
  candidatos = Candidatos.objects.get(pk = id)
  candidatos.delete()
  return redirect('http://127.0.0.1:8000/candidatos')

@unauthenticated_user
def loginPage(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username = username, password = password)

    if user is not None:
      login(request, user)
      return redirect('http://127.0.0.1:8000/home')
    else: 
      messages.info(request, 'Username or Password is incorrect!')

  context = {}
  return render(request, 'crudrh/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('http://127.0.0.1:8000/login')

@unauthenticated_user
def registerPage(request):
  form = CreateUserForm()
  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')

      group = Group.objects.get(name = 'candidato')
      user.groups.add(group)

      messages.success(request, f"El usuario {username} ha sido creado!")

  context = {'form':form}
  return render(request, 'crudrh/register.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
@allowed_users(allowed_roles = ['candidato'])
def userPage(request):
    context = {}
    return render(request, 'crudrh/user.html', context) 
 
 



