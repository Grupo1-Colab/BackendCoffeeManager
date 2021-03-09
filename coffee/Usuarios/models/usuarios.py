from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario (AbstractUser):
    '''
        La clase Usuario hereda de AbstractUser, propia de Django, para poder
        crear más fácil al usuario.
        Otorga campos como first_name, last_name, etc.
    '''
    # Constantes para los roles de los usuarios
    ADMINISTRADOR = 1
    MESERO = 2
    
    #Constante de ROLES
    ROLES = (
        (ADMINISTRADOR, 'Administrador'),
        (MESERO, 'Mesero'),
    )
    
    #Campos
    username = models.CharField(
        'username',
        max_length = 50,
        unique = True,
        error_messages = {
            'unique' : 'Ya existe un usuario con este nombre de usuario.'
        }
    )
    USERNAME_FIELD = 'username'
    
    email = models.EmailField(
        'email_address',
        unique = True,
        error_messages = {
            'unique' : 'Ya existe un usuario con este correo.'
        }
    )
    rol = models.IntegerField(choices=ROLES, default=MESERO)
    is_verified = models.BooleanField(
        'usuario',
        default=True
    )
    is_active = models.BooleanField(default=True)
    
    if rol == 1:
        is_staff = models.BooleanField(default=False)
    else:
        is_staff = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username