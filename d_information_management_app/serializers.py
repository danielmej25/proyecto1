from rest_framework import serializers
from .views import Pais

class paisSerializer(serializers.ModelSerializer):
    class META():
        model=Pais
        campos=('nombre')
