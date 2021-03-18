from django.urls import path
#Vistas
from .views.usuarios import CrearUsuario, ListarUsuarios, ActualizarUsuario, EliminarUsuario, VerUsuario, LoginView
from .views.clientes import CrearCliente, ListarClientes, ActualizarCliente, EliminarCliente, VerCliente, VerPerfilNit, VerActualizarPerfilNit, VerPerfilesNit

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    #URLs de Usuarios
    path('usuarios/crear', CrearUsuario.as_view(), name='crearUsuario'),
    path('usuarios/listar', ListarUsuarios.as_view(), name='listarUsuarios'),
    path('usuarios/actualizar/<pk>', ActualizarUsuario.as_view(), name='actualizarUsuario'),
    path('usuarios/eliminar/<pk>', EliminarUsuario.as_view(), name='eliminarUsuario'),
    path('usuarios/ver/<pk>', VerUsuario.as_view(), name='verUsuario'),
    #URLs de Clientes
    path('clientes/crear', CrearCliente.as_view(), name='crearCliente'),
    path('clientes/listar', ListarClientes.as_view(), name='listarclientes'),
    path('clientes/actualizar/<pk>', ActualizarCliente.as_view(), name='actualizarCliente'),
    path('clientes/eliminar/<pk>', EliminarCliente.as_view(), name='eliminarCliente'),
    path('clientes/ver/<pk>', VerCliente.as_view(), name='verCliente'),
    #Perfiles Nit
    path('clientes/nit/usuarioActual', VerActualizarPerfilNit.as_view(), name='nitUsuario'),
    path('clientes/nit/general', VerPerfilesNit.as_view(), name='nits'),
    path('clientes/nit/<pk>', VerPerfilNit.as_view(), name='verNit'),
]