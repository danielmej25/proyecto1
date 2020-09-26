from django.urls import path, include
from .views import crearPais, crear_grupo_investigacion

urlpatterns = [
    path('crear_pais/', crearPais, name='crear_pais'),
    path('crear_grupo_inv/', crear_grupo_investigacion, name='crear_grupo_inv'),
    #path('crear_gi/', crear_gi, name='crear_gi'),
]

#http://localhost:8000/information/crear_gi/12/13/14/15/Grupo1/1999/algunacosa/cat1