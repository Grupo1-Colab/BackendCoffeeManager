from django.db import models

class Pedido (models.Model):
    '''
        Clase para poder almacenar un pedido
        con la información necesaria
    '''
    #Constantes de Tipo
    EFECTIVO = 1
    TARJETA = 2
    
    TIPO = (
        (EFECTIVO, 'Pago en efectivo'),
        (TARJETA, 'Pago con tarjeta'),
    )
    #Campos
    tipo_pago = models.IntegerField(choices=TIPO)
    producto = models.ForeignKey('Productos.Producto', on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey('Usuarios.Cliente', on_delete=models.DO_NOTHING)

class Factura (models.Model):
    createdAt = models.DateTimeField(auto_now=True)
    total = models.FloatField()
    pedido = models.OneToOneField(Pedido, on_delete=models.DO_NOTHING)