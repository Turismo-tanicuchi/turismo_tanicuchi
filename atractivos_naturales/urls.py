from django.urls import path
from django.contrib.auth.decorators import login_required
from atractivos_naturales.views import ListarAtractivoNatural,ActualizarAtractivoNatural,EliminarAtractivoNatural
from atractivos_naturales import views

urlpatterns = [
    path('listar_atractivos_natural/',login_required(ListarAtractivoNatural.as_view()),name ='listado_atractivos'),
    #path('registrar_atractivo/',login_required(RegistrarAtractivoNatural.as_view()),name ='registrar_atractivo'),
    path('registrar_atractivo/',login_required(views.registrarAtractivoNatural),name ='registrar_atractivo'),
    path('editar_atractivo_natural/<int:pk>/',login_required(ActualizarAtractivoNatural.as_view()), name = 'editar_atractivo'),
    path('eliminar_atractivo_natural/<int:pk>/',login_required(EliminarAtractivoNatural.as_view()), name = 'eliminar_atractivo'),
]
