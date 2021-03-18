from rest_framework import serializers
#Modelo
from ..models.categorias import Categorias

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'