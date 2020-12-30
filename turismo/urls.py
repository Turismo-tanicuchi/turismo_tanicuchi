from django.contrib import admin
from django.urls import path
#agregadas de configuraciones de static y media
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
#agregadas de apps y models
from .import views
from parroquias.views import ParroquiasListView
from usuario.views import Login,logoutUsuario
from django.contrib.auth.decorators import login_required
from usuario.views import RegistrarUsuario,MisDatos,ActualizarUsuario,EliminarUsuario,ActualizarPasswordUsuario

urlpatterns = [

    #administrador de django
    path('admin/', admin.site.urls),
    #sitio-administrador
    path('administrador/index', login_required(views.home_view), name='home'),
    #************************ dedicadas al usuario ******************
    path('usuarios/',include(('usuario.urls','usuarios'))),
    path('accounts/login/', Login.as_view(), name= 'login'),
    path('logout/',login_required(logoutUsuario), name= 'logout'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name ='registrar_usuario'),
    path('mis_datos/',login_required(MisDatos.as_view()),name ='mis_datos'),
    path('editar_mis_datos/<int:pk>/',login_required(ActualizarUsuario.as_view()),name ='editar_mis_datos'),
    path('eliminar_mis_datos/<int:pk>/',login_required(EliminarUsuario.as_view()),name ='eliminar_mis_datos'),
    path('editar_password/<int:pk>/',login_required(ActualizarPasswordUsuario.as_view()),name ='editar_password'),
    #********************** ruta de la app parroquias****************
    path('parroquias/',include(('parroquias.urls','parroquias'))),
    #********************** ruta de atarctivos Naturales*************
    path('atractivos_naturales/',include(('atractivos_naturales.urls','atractivos_naturales'))),
    #********************** ruta de atarctivos Culturales*************
    path('atractivos_culturales/',include(('atractivos_culturales.urls','atractivos_culturales'))),
    #********************** ruta de alojamiento*************
    path('alojamiento/',include(('alojamiento.urls','alojamiento'))),
    #********************** ruta de transporte*************
    path('transporte/',include(('transporte.urls','transporte'))),
    #********************** ruta de empresa*************
    path('empresa/',include(('empresa.urls','empresa'))),
    #********************** ruta de restaurante*************
    path('restaurante/',include(('restaurante.urls','restaurante'))),
    #************************ Index Turista **********************
    path('', views.index_view, name='index'),
    path('turista/',include(('interfaz_turista.urls','turista'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
