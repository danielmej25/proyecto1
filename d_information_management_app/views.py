from django.shortcuts import render, redirect
from .forms import PaisForm
from .models import grupo_investigacion
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import sqlite3

# Create your views here.

def home(request):
    return render(request,'index.html')

def crearPais(request):
    if request.method == 'POST':
        print(request.POST)
        pais_form = PaisForm(request.POST)

        if pais_form.is_valid():
            pais = pais_form.cleaned_data['nombre']
            print("El nombre del pais es: ",pais)
            pais_form.save()
        return redirect('index')
    else:
        pais_form = PaisForm()
    return render(request, 'pais/crear_pais.html',{'pais_form':pais_form})

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
