#General
from django.shortcuts import render, redirect

#Jeison
from .models import grupo_investigacion
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import sqlite3

#Javier
from .forms import PaisForm, DepartamentoForm, CiudadForm
from .models import Pais


# Create your views here.


#--------------------------------------------JAVIER

def home(request):
    return render(request,'index.html')

def crearPais(request):
    if request.method == 'POST':
        pais_form = PaisForm(request.POST)
        if pais_form.is_valid():
            pais = pais_form.cleaned_data['nombre']
            pais_form.save()
        return redirect('index')
    else:
        pais_form = PaisForm()
    return render(request, 'pais/crear_pais.html',{'pais_form':pais_form})

def consultarPais(request):
    autor_form = None
    error = None
    paises = None
    if request.method == 'POST':
        pais_form = PaisForm(request.POST)
        if pais_form.is_valid():
            nombre = pais_form.cleaned_data['nombre']
            paises = Pais.objects.filter(nombre__iexact = nombre)
    else:
        pais_form = PaisForm()
    return render(request, 'pais/consultar_pais.html',{'pais_form':pais_form, 'paises':paises, 'error':error})
        

def crearDepartamento(request):
    if request.method == 'POST':
        departamento_form = DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento = departamento_form.cleaned_data['nombre']
            departamento_form.save()
        return redirect('index')
    else:
        departamento_form = DepartamentoForm()
    return render(request, 'departamento/crear_departamento.html',{'departamento_form':departamento_form})


def crearCiudad(request):
    if request.method == 'POST':
        ciudad_form = CiudadForm(request.POST)
        if ciudad_form.is_valid():
            ciudad = ciudad_form.cleaned_data['nombre']
            ciudad_form.save()
        return redirect('index')
    else:
        ciudad_form = CiudadForm()
    return render(request, 'ciudad/crear_ciudad.html',{'ciudad_form':ciudad_form})


#--------------------------------------------JEISON

# Metodo para la creacion de un objeto de la clase Grupo de Investigacion
def crear_grupo_investigacion(request):

    if request.method=="POST" and request.POST["id_ins"]:
        bandera = "correcto"
        id_instit = request.POST["id_ins"]
        nombre_gi = request.POST["name_gi"]
        categoria = request.POST["categoria"]
        email = request.POST["email"]
        fundacion_grupo = request.POST["fund_grupo"]

        gi1=grupo_investigacion(id_institucion=id_instit , nombre_grupo_inv=nombre_gi, fundacion_grupo=fundacion_grupo, email=email, categoria=categoria)
        gi1.save()
        return render(request, "pais/crear_pais.html",{"bandera":bandera})
    else:
        return render(request, "grupo_investigacion/crear_gi.html")
