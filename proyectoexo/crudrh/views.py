from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import *

@login_required(login_url= "http://127.0.0.1:8000/login")
def home(request):
    return render(request, 'crudrh/home_page.html')

@login_required(login_url= "http://127.0.0.1:8000/login")
def competencias(request):
  competencias = Competencias.objects.all()
  return render(request, 'crudrh/competencias.html', {'competencias' : competencias})

@login_required(login_url= "http://127.0.0.1:8000/login")
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
def updateCompetencias(request):
  form = CompetenciasForm()
  context = { 'form':form }
  return render(request, 'crudrh/competencias_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
def idiomas(request):
  idiomas = Idiomas.objects.all()
  return render(request, 'crudrh/idiomas.html', {'idiomas' : idiomas})

@login_required(login_url= "http://127.0.0.1:8000/login")
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
def capacitaciones(request):
  capacitaciones = Capacitaciones.objects.all()
  return render(request, 'crudrh/capacitaciones.html', {'capacitaciones' : capacitaciones})

@login_required(login_url= "http://127.0.0.1:8000/login")
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
def puestos(request):
  puestos = Puestos.objects.all()
  return render(request, 'crudrh/puestos.html', {'puestos' : puestos})

@login_required(login_url= "http://127.0.0.1:8000/login")
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
def experiencia_laboral(request):
  experiencia_laboral = Experiencia_Laboral.objects.all()
  return render(request, 'crudrh/experiencia_laboral.html', {'experiencia_laboral' : experiencia_laboral})

@login_required(login_url= "http://127.0.0.1:8000/login")
def createExperiencia_laboral(request):
  form = Experiencia_LaboralForm()
  context = { 'form':form }
  if request.method == 'POST':
    form = Experiencia_LaboralForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/experiencia_laboral')
  return render(request, 'crudrh/experiencia_laboral_form.html', context)

@login_required(login_url= "http://127.0.0.1:8000/login")
def empleados(request):
  empleados = Empleados.objects.all()
  return render(request, 'crudrh/empleados.html', {'empleados' : empleados})

@login_required(login_url= "http://127.0.0.1:8000/login")
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


def loginPage(request):
  if request.user.is_authenticated:
    return redirect('http://127.0.0.1:8000/home')
  else:
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

def registerPage(request):
  if request.user.is_authenticated:
    return redirect('http://127.0.0.1:8000/home')
  else: 
    form = CreateUserForm()
    if request.method == "POST":
      form = CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, "El usuario " + user + " ha sido creado!")

    context = {'form':form}
    return render(request, 'crudrh/register.html', context)

def userPage(request):
  context = {}
  return render(request, 'crudrh/user.html', context) 