from rest_framework import serializers
from .models import Pais


class PaisSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()

    def create(self, validate_data):
        instance = Pais()
        instance.nombre = validate_data.get('nombre')
        instance.save()
        return instance
    """
    def validate_username(self, data):
        paises = Pais.objects.filter(nombre = data)
        if len(paises) != 0:
            raise serializers.ValidationError("Este nombre de pais ya existe, Ingrese uno nuevo")
        else:
            return data
    """

    def update(self,instance, validated_data):
        instace.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()
        return instance