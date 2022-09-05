from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CandidatosForm(ModelForm):
    class Meta:
      model = Candidatos
      fields = '__all__'

class EmpleadosForm(ModelForm):
    class Meta:
      model = Empleados
      fields = '__all__'

class CompetenciasForm(ModelForm):
    class Meta:
      model = Competencias
      fields = '__all__'

class IdiomasForm(ModelForm):
    class Meta:
      model = Idiomas
      fields = '__all__'

class CapacitacionesForm(ModelForm):
    class Meta:
      model = Capacitaciones
      fields = '__all__'

class PuestosForm(ModelForm):
    class Meta:
      model = Puestos
      fields = '__all__'

class Experiencia_LaboralForm(ModelForm):
    class Meta:
      model = Experiencia_Laboral
      fields = '__all__'

    class Meta:
      model = Experiencia_Laboral
      fields = '__all__'

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']