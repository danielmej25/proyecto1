from django.db import models

# Create your models here.
# Zona Arias

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
    
    def __str__(self):
        return self.nombre

#---------------------------------------------------------------------------------------------------------------------------------------------
# Zona Jeison
# Clase que contiene la informacion basica de los Grupos de Investigacion
class grupo_investigacion(models.Model):
    id_grupo_investigacion = models.AutoField(primary_key=True)
    id_institucion = models.IntegerField()
    nombre_grupo_inv = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    email = models.EmailField()
    fundacion_grupo = models.DateField()

    class Meta:
        verbose_name = 'Grupo de investigación'
        verbose_name_plural = 'Grupos de investigación'

    def __str__(self):
        return self.nombre_grupo_inv