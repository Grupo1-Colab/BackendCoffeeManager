#Serializador
from ..serializers.productos import ProductosSerializer
#Modelo
from ..models.productos import Producto
#Autenticación
from rest_framework.permissions import IsAdminUser
#Vistas Genéricas
from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView,
                                    UpdateAPIView,
                                    DestroyAPIView)

class CrearProducto(CreateAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductosSerializer
    model = Producto
    permission_classes = [IsAdminUser]

class ListarProductos (ListAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductosSerializer
    model = Producto
    permission_classes = []

class ActualizarProducto (UpdateAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductosSerializer
    model = Producto
    permission_classes = [IsAdminUser]

class EliminarProducto (DestroyAPIView):
    queryset = Producto.objects.all().order_by('-createdAt')
    serializer_class = ProductosSerializer
    model = Producto
    permission_classes = [IsAdminUser]