from django.urls import path
from django.contrib.auth.decorators import login_required
from empresa.views import ListarCategoriasEmpresa
from empresa.views import ActualizarCategoriaEmpresa,EliminarCategoriaEmpresa
from empresa.views import ListarEmpresa,EliminarEmpresa
from empresa.views import ListarProducto,EliminarProducto

from empresa import views

urlpatterns = [
    #**************************Categorias*******************************************
    path('listado_categorias_empresa/',login_required(ListarCategoriasEmpresa.as_view()),name ='listado_categorias_empresa'),
    path('registrar_categoria/',login_required(views.registrarCategoriaEmpresa),name ='registrar_categoria'),
    path('editar_categoria/<int:pk>/',login_required(ActualizarCategoriaEmpresa.as_view()), name = 'editar_categoria'),
    path('eliminar_categoria/<int:pk>/',login_required(EliminarCategoriaEmpresa.as_view()), name = 'eliminar_categoria'),
    #**************************Empresas*******************************************
    path('listar_empresa/',login_required(ListarEmpresa.as_view()),name ='listado_empresa'),
    path('registrar_empresa/',login_required(views.registrarEmpresa),name ='registrar_empresa'),
    path('editar_empresa/<int:id>/',login_required(views.actualizarEmpresa), name = 'editar_empresa'),
    path('eliminar_empresa/<int:pk>/',login_required(EliminarEmpresa.as_view()), name = 'eliminar_empresa'),
    #**************************productos*******************************************
    path('listar_producto/',login_required(ListarProducto.as_view()),name ='listado_producto'),
    path('registrar_producto/',login_required(views.registrarProducto),name ='registrar_producto'),
    path('editar_producto/<int:id>/',login_required(views.actualizarProducto), name = 'editar_producto'),
    path('eliminar_producto/<int:pk>/',login_required(EliminarProducto.as_view()), name = 'eliminar_producto'),
]
