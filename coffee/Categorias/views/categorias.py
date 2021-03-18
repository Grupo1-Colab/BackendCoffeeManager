##Serializador
from ..serializers.categorias import CategoriasSerializer
#Modelo
from ..models.categorias import Categorias
#Autenticación
from rest_framework.permissions import IsAdminUser
#Vistas Genéricas
from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView,
                                    UpdateAPIView,
                                    DestroyAPIView)

class CrearCategorias(CreateAPIView):
    queryset = Categorias.objects.all().order_by('-createdAt')
    serializer_class = CategoriasSerializer
    model = Categorias
    permission_classes = [IsAdminUser]

class ListarCategoriass (ListAPIView):
    queryset = Categorias.objects.all().order_by('-createdAt')
    serializer_class = CategoriasSerializer
    model = Categorias
    permission_classes = []

class ActualizarCategorias (UpdateAPIView):
    queryset = Categorias.objects.all().order_by('-createdAt')
    serializer_class = CategoriasSerializer
    model = Categorias
    permission_classes = [IsAdminUser]

class EliminarCategorias (DestroyAPIView):
    queryset = Categorias.objects.all().order_by('-createdAt')
    serializer_class = CategoriasSerializer
    model = Categorias
    permission_classes = [IsAdminUser]