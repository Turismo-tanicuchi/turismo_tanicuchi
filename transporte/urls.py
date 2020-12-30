from django.urls import path
from django.contrib.auth.decorators import login_required
from transporte.views import ListarTransporte,ActualizarTransporte,EliminarTransporte
from transporte import views

urlpatterns = [
    path('listar_transporte/',login_required(ListarTransporte.as_view()),name ='listado_transporte'),
    path('registrar_transporte/',login_required(views.registrarTransporte),name ='registrar_transporte'),
    path('editar_transporte/<int:pk>/',login_required(ActualizarTransporte.as_view()), name = 'editar_transporte'),
    path('eliminar_transporte/<int:pk>/',login_required(EliminarTransporte.as_view()), name = 'eliminar_transporte'),
]
