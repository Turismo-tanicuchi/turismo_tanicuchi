from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from parroquias.views import MostrarDatosParroquia,ActualizarDatosParroquia,MostrarImagenesParroquia,EliminarImagenesParroquia

urlpatterns = [
    path('',views.ParroquiasListView.as_view(), name='listado_parroquias'),
    path('search', views.ParroquiaSearchListView.as_view(), name='search'),
    path('<slug:slug>',views.ParroquiaDetailView.as_view(),name='parroquia'),
    path('datos_parroquia/',login_required(MostrarDatosParroquia.as_view()),name ='datos_parroquia'),
    path('img_parroquia/',login_required(MostrarImagenesParroquia.as_view()),name ='img_parroquia'),
    path('cargar_imagenes/',login_required(views.registrarImagenes),name ='cargar_imagenes'),
    path('eliminar_imagen/<int:pk>/',login_required(EliminarImagenesParroquia.as_view()), name = 'eliminar_imagen'),
    path('editar_parroquia/<int:pk>/',login_required(ActualizarDatosParroquia.as_view()), name = 'editar_parroquia'),
]
