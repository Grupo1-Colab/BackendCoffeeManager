#Serializador
from ..serializers.clientes import ClienteSerializer, PerfilNitSerializer
#Modelos
from ..models.clientes import Cliente, PerfilNit
#Respuesta de servidor
from rest_framework.response import Response
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated
#Vistas Genéricas
from rest_framework.generics import (ListAPIView, 
                                    RetrieveUpdateAPIView,
                                    get_object_or_404,
                                    CreateAPIView,
                                    RetrieveAPIView,
                                    UpdateAPIView,
                                    DestroyAPIView
                                    )
from rest_framework import status
from rest_framework.views import APIView

class CrearCliente(CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    model = Cliente
    permission_classes = []

class ListarClientes (ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    model = Cliente
    permission_classes = []

class ActualizarCliente (UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    model = Cliente
    permission_classes = [IsAdminUser]

class EliminarCliente (DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    model = Cliente
    permission_classes = [IsAdminUser]

class VerCliente (RetrieveAPIView):
    serializer_class = ClienteSerializer
    model = Cliente
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = Cliente.objects.all()
        identificacion = self.kwargs['pk']
        return query.filter(id=identificacion)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

class VerPerfilesNit (ListAPIView):
    queryset = PerfilNit.objects.all()
    serializer_class = PerfilNitSerializer
    model = PerfilNit
    permission_classes = [IsAuthenticated, IsAdminUser]

class VerActualizarPerfilNit (RetrieveUpdateAPIView):
    serializer_class = PerfilNitSerializer
    lookup_field = 'id'
    
    def get_serializer_context(self):
        context = super(VerActualizarPerfilNit, self).get_serializer_context()
        return context

    def get_queryset(self):
        qs = PerfilNit.objects.all()
        logged_in_user_profile = qs.filter(usuario=self.request.user)
        return logged_in_user_profile
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, usuario=self.request.user)
        return obj

class VerPerfilNit (RetrieveAPIView):
    serializer_class = PerfilNitSerializer
    model = PerfilNit
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        query = PerfilNit.objects.all()
        identificacion = self.kwargs['pk']
        return query.filter(id=identificacion)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj