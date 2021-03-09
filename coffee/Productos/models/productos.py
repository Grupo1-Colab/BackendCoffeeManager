from django.db import models

class Producto (models.Model):
    '''
        La clase Producto tendrá los campos necesarios
        para los productos de la cafetería.
    '''
    #Constantes para los ESTADOS de los productos
    ACTIVO = 1
    INACTIVO = 0
    
    ESTADO = (
        (ACTIVO, 'Producto disponible'),
        (INACTIVO, 'Producto no disponible')
    )
    nombre = models.CharField(max_length = 255)
    descripcion = models.TextField(blank=True)
    precio = models.FloatField()
    estado = models.IntegerField(choices=ESTADO, default=ACTIVO)
    createdAt = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey('Categorias.Categorias', on_delete=models.DO_NOTHING)
    