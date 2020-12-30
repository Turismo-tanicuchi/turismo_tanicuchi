from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import ListadoUsuario,AdminEliminarUsuario
#,RegistrarUsuario,ActualizarUsuario,

urlpatterns = [
    path('listado_usuarios/', login_required(ListadoUsuario.as_view()),name='listar_usuarios'),
    #path('registrar_usuario/',login_required(RegistrarUsuario.as_view()),name ='registrar_usuario'),
    #path('editar_usuario/<int:pk>/',login_required(ActualizarUsuario.as_view()), name = 'editar_usuario'),
    path('admin_eliminar_usuario/<int:pk>/',login_required(AdminEliminarUsuario.as_view()), name = 'admin_eliminar_usuario'),

]
