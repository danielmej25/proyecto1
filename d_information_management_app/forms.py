#General
from django import forms

#Javier
from .models import Pais, Departamento, Ciudad

#Jeison

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['pais', 'nombre']

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['pais','departamento','nombre']
