from rest_framework import serializers
#Modelo
from ..models.productos import Producto
#Serializador
from Categorias.serializers.categorias import CategoriasSerializer

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombre', 'descripcion', 'precio', 'estado', 'createdAt', 'categoria']