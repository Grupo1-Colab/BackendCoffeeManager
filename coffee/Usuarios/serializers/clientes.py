from rest_framework import serializers
#Modelo
from ..models.clientes import Cliente, PerfilNit

class PerfilNitSerializer(serializers.ModelSerializer):
    """
        Serializador de NIT asociado a algún cliente.
    """
    class Meta:
        model = PerfilNit
        fields = ['cliente']
        read_only_fields = ['creado', 'modificado']

class ClienteSerializer(serializers.ModelSerializer):
    nit = PerfilNitSerializer(read_only = True)
    
    class Meta:
        model = Cliente
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'nit', 'is_verified', 'is_active']
    
    def create(self, validated_data):
        cliente = Cliente(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email']
        )
        cliente.save()
        
        nitDefault = 00000
        PerfilNit.objects.create(cliente = cliente, numNit = nitDefault)
        
        return cliente