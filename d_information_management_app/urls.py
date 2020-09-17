from django.urls import path, include
from .views import crearPais

urlpatterns = [
    path('crear_pais/', crearPais, name='crear_pais')
]