from django.shortcuts import render, redirect
from .forms import PaisForm
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


    