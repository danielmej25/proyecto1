from rest_framework import serializers
from .models import Pais, GrupoInvestigacion


class PaisSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()

    def create(self, validate_data):
        instance = Pais()
        instance.nombre = validate_data.get('nombre')
        instance.save()
        return instance
<<<<<<< HEAD
    """
    def validate_username(self, data):
=======
    
    """def validate_username(self, data):
>>>>>>> 48531c9773ea7d85910c245a4788bb2a082b5638
        paises = Pais.objects.filter(nombre = data)
        if len(paises) != 0:
            raise serializers.ValidationError("Este nombre de pais ya existe, Ingrese uno nuevo")
        else:
<<<<<<< HEAD
            return data
    """

    def update(self,instance, validated_data):
        instace.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()
        return instance
=======
            return data"""

class GrupoInvestigacionSerializer(serializers.Serializer):
    id_grupo_investigacion = serializers.ReadOnlyField()
    id_institucion = serializers.IntegerField()
    nombre_grupo_inv = serializers.CharField()
    categoria = serializers.CharField()
    email = serializers.EmailField()
    fundacion_grupo = serializers.DateField()

    def create(self, validate_data):
        instance = grupo_investigacion()
        instance.id_institucion = validate_data.get('id_institucion')
        instance.nombre = validate_data.get('nombre')
        instance.categoria = validate_data.get('categoria')
        instance.email = validate_data.get('email')
        instance.fecha_fundacion = validate_data.get('fecha_fundacion')
        instance.save()
        return instance
>>>>>>> 48531c9773ea7d85910c245a4788bb2a082b5638
