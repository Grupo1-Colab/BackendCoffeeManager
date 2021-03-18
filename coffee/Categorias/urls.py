from django.urls import path
#Vistas
from .views.categorias import CrearCategorias, ListarCategoriass, EliminarCategorias, ActualizarCategorias

urlpatterns = [
    path('categoria/crear', CrearCategorias.as_view(), name='crearCategoria'),
    path('categoria/listar', ListarCategoriass.as_view(), name='listarCategorias'),
    path('categoria/eliminar/<pk>', EliminarCategorias.as_view(), name='eliminarCategoria'),
    path('categoria/actualizar/<pk>', ActualizarCategorias.as_view(), name='actualizarCategoria'),
]
