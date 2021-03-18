from rest_framework import serializers
#Modelos
from ..models.usuarios import Usuario
#Token de RestFramework
from rest_framework.authtoken.models import Token

class UsuarioSerializer (serializers.ModelSerializer):
    """
        Serializador de los usuarios del sistema.
    """
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'rol', 'is_staff']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
        depth = 1
    
    def create(self, validated_data):
        user = Usuario(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            rol = validated_data['rol'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        
        return user