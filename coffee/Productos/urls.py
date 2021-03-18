from django.urls import path
#Vistas
from .views.productos import CrearProducto, ListarProductos, EliminarProducto, ActualizarProducto

urlpatterns = [
    path('producto/crear', CrearProducto.as_view(), name='crearProducto'),
    path('producto/listar', ListarProductos.as_view(), name='listarProductos'),
    path('producto/actualizar/<pk>', ActualizarProducto.as_view(), name='actualizarProducto'),
    path('producto/eliminar/<pk>', EliminarProducto.as_view(), name='eliminarProducto'),
]
