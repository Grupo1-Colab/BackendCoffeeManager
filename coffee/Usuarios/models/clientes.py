from django.db import models

class Cliente (models.Model):
    '''
        La clase Cliente también hereda de AbstractUser, para poder crear a un usuario.
    '''
    #Constante para el CLiente
    CLIENTE = 1
    
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
    tipo = models.IntegerField(default=CLIENTE)
    is_verified = models.BooleanField(
        'cliente',
        default=True
    )
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username

class Inicio (models.Model):
    '''
        Clase para poder integrar fechas de creación y modificación.
    '''
    creado = models.DateTimeField(
        'creado el', auto_now_add=True, help_text='Fecha en la que se registró.'
    )
    modificado = models.DateTimeField(
        'modificado el', auto_now=True, help_text='Fecha en la que se modificó.'
    )
    
    class Meta:
        abstract=True

class PerfilNit (Inicio):
    '''
        Hereda de Inicio para poder obtener las fechas de creación,
        y solamente se liga a un Cliente en específico.
    '''
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.cliente)