from django.db import models

# Create your models here.


class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
    
    def __str__(self):
        return self.nombre