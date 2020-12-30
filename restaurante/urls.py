from django.urls import path
from django.contrib.auth.decorators import login_required
from restaurante.views import ListarRestaurante,ActualizarRestaurante, EliminarRestaurante
from restaurante import views

urlpatterns = [
    path('listar_restaurantes/',login_required(ListarRestaurante.as_view()),name ='listar_restaurantes'),
    path('registrar_restaurante/',login_required(views.registrarRestaurante),name ='registrar_restaurante'),
    path('editar_restaurante/<int:pk>/',login_required(ActualizarRestaurante.as_view()), name = 'editar_restaurante'),
    path('eliminar_restaurante/<int:pk>/',login_required(EliminarRestaurante.as_view()), name = 'eliminar_restaurante'),
]
