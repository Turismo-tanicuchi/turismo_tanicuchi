from django.urls import path
from superadministracion import views
from django.contrib.auth.decorators import login_required
from superadministracion.views import ListadoUsuario,CrearUsuario,ActualizarUsuario,EliminarUsuario,ActualizarPasswordUsuario
from superadministracion.views import MostrarParroquias,EliminarParroquia

urlpatterns = [
    path('superadmin', login_required(views.home_superadmin), name='superadmin'),
    path('mostrar_usuarios/', login_required(ListadoUsuario.as_view()),name='mostrar_usuarios'),
    path('crear_usuario/',login_required(CrearUsuario.as_view()),name ='crear_usuario'),
    path('editar_usuario/<int:pk>/',login_required(ActualizarUsuario.as_view()), name = 'editar_usuario'),
    path('eliminar_usuario/<int:pk>/',login_required(EliminarUsuario.as_view()), name = 'eliminar_usuario'),
    path('nueva_password/<int:pk>/',login_required(ActualizarPasswordUsuario.as_view()), name = 'nueva_password'),
    #parroquias
    path('mostrar_parroquias/', login_required(MostrarParroquias.as_view()),name='mostrar_parroquias'),
    path('crear_parroquia/',login_required(views.registrar_parroquia),name ='crear_parroquia'),
    path('editar_parroquia/<int:id>/',login_required(views.actualizarparroquia), name = 'editar_parroquia'),
    path('eliminar_parroquia/<int:pk>/',login_required(EliminarParroquia.as_view()), name = 'eliminar_parroquia'),
]
