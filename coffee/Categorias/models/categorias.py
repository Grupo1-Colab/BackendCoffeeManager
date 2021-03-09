from django.db import models

class Categorias (models.Model):
    '''
        Clase para las Categorías de los platillos de la cafetería
    '''
    #Constantes de posibles categorías
    NODEF = 0
    ENTRADA = 1
    PLATO_FUERTE = 2
    BEBIDA_SA = 3
    BEBIDA_CA = 4
    POSTRE = 5
    REFACCION = 6
    
    #Categorías
    CATEGORIAS = (
        (ENTRADA, 'Platillo de entrada'),
        (PLATO_FUERTE, 'Plato fuerte'),
        (POSTRE, 'Postre'),
        (REFACCION, 'Refacción'),
        (BEBIDA_SA, 'Bebida sin alcohol'),
        (BEBIDA_CA, 'Bebida con alcohol'),
        (NODEF, 'Sin definir'),
    )
    #Campos
    tipo = models.IntegerField(choices=CATEGORIAS, default=NODEF)
    descripcion = models.CharField(max_length = 255)
    createdAt = models.DateTimeField(auto_now=True)