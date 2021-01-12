from django.urls import path
from .import views
from .views import ImagenesAtrNatural
urlpatterns = [
    #datos de la parroquia
    #path('datos_generales/<slug:slug>',DatosParroquiaView.as_view(),name ='datos_generales'),
    path('datos_generales/<slug:slug>/', views.datos_parroquia, name='datos_generales'),
    path('datos_parroquia/', views.datos_generales, name='datos_parroquia'),
    #*Bryan Sandoval IMPLEMENTACION DE ubicacion de la parroquia**
    path('ubicacion_parroquia/', views.ubicacion_parroquia, name='ubicacion_parroquia'),
    #****** fin de implementacion *****************
    #turismo de la parroquia
    path('turismo/',views.turismo,name ='turismo'),
    path('atractivos_naturales/', views.atractivos_naturales, name='atractivos_naturales'),
    #*Bryan Sandoval IMPLEMENTACION DE MAPAS atractivo naturales**
    path('ver_ubicacion/<int:id>', views.ver_ubicacion, name='ver_ubicacion'),
    #****** fin de implementacion *****************
    path('atractivos_culturales/', views.atractivos_culturales, name='atractivos_culturales'),
    #*Bryan Sandoval IMPLEMENTACION DE MAPAS atractivo culturales**
    path('ver_ubicacion2/<int:id>', views.ver_ubicacion2, name='ver_ubicacion2'),
    #****** fin de implementacion *****************
    path('alojamiento/', views.alojamientos, name='alojamiento'),
    #*Bryan Sandoval IMPLEMENTACION DE MAPAS alojamiento**
    path('ver_ubicacion3/<int:id>', views.ver_ubicacion3, name='ver_ubicacion3'),
    #****** fin de implementacion *****************
    path('restaurantes/', views.restaurantes, name='restaurantes'),
    path('transporte/', views.transporte, name='transporte'),
    #*Bryan Sandoval IMPLEMENTACION DE MAPAS alojamiento**
    path('ver_ubicacion4/<int:id>', views.ver_ubicacion4, name='ver_ubicacion4'),
    #****** fin de implementacion *****************
    #fomento productivo de la parroquia
    path('fomento_productivo/',views.fomento_productivo,name ='fomento_productivo'),
    path('empresas/<int:id>',views.empresas,name ='empresas'),
    #*Bryan Sandoval IMPLEMENTACION DE MAPAS empresa**
    path('ubicacion_empresa/<int:id>', views.ubicacion_empresa, name='ubicacion_empresa'),
    #****** fin de implementacion *****************
    path('productos/<int:id>',views.productos,name ='productos'),
    path('actividades/',views.actividades,name ='actividades'),
    path('imagenes/',ImagenesAtrNatural.as_view(),name ='imagenes'),
    # vista de mapa turistico
    path('mapa_turistico/',views.mapa_turistico,name ='mapa_turistico'),
]
