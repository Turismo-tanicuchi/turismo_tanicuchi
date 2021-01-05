from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from parroquias.models import Parroquia,ImagenesParroquia
from django.views.generic import TemplateView
from atractivos_naturales.models import ImagenesAtractivoNatural
from django.shortcuts import render
from atractivos_naturales.models import AtractivoNatural,ImagenesAtractivoNatural
from atractivos_culturales.models import AtractivoCultural
from alojamiento.models import Alojamiento
from empresa.models import TipoEmp,Empresa,Producto
from restaurante.models import Restaurante
from django.http import JsonResponse
# Create your views here.
#class DatosParroquiaView(DetailView):
#    model = Parroquia
#    template_name = 'interfaz_turista/datos_generales.html'
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        consulta_imagenes = ImagenesParroquia.objects.filter(parroquia__slug=self.kwargs['slug'])
#        context['imagenes'] = consulta_imagenes
#        return context

#para poder usar sesiones
def datos_parroquia(request, slug):
    info_parroquia=Parroquia.objects.filter(slug=slug)
    consulta_imagenes = ImagenesParroquia.objects.filter(parroquia__slug=slug)
    request.session['parroquia_id']=slug
    valor = request.session.get('parroquia_id')
    #print(valor)
    productos=Producto.objects.filter(empresa__tipo_id__parroquia__slug=slug)[:7]
    return render(request,'interfaz_turista/datos_generales.html',{
        'mostrar_parroquia':info_parroquia,
        'mostrar_imagenes' : consulta_imagenes,
        'mostrar_productos':productos,
    })

#cuando no viene el slug de la pqrroquia uso el q tiene la sesion
def datos_generales(request):
    valor = request.session.get('parroquia_id')
    #print(valor)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    consulta_imagenes = ImagenesParroquia.objects.filter(parroquia__slug=valor)
    productos=Producto.objects.filter(empresa__tipo_id__parroquia__slug=valor)[:7]
    return render(request,'interfaz_turista/datos_generales.html',{
        'mostrar_parroquia':info_parroquia,
        'mostrar_imagenes' : consulta_imagenes,
        'mostrar_productos':productos,
    })

def turismo(request):
    valor = request.session.get('parroquia_id')
    info_parroquia=Parroquia.objects.filter(slug=valor)
    productos=Producto.objects.filter(empresa__tipo_id__parroquia__slug=valor)[:7]
    return render(request,'interfaz_turista/turismo.html',{
        'mostrar_productos':productos,
        'mostrar_parroquia':info_parroquia,
    })

def atractivos_naturales(request):
    valor = request.session.get('parroquia_id')
    #print(valor)
    atrac_naturales=AtractivoNatural.objects.filter(parroquia__slug=valor)
    #print(atrac_naturales)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    #consulta_imagenes = ImagenesAtractivoNatural.objects.filter(atractivonatural__id=atrac_naturales.id)
    #print(atrac_naturales)
    return render(request,'interfaz_turista/atrac_natural.html',{
        'mostrar_atractivos':atrac_naturales,
        'mostrar_parroquia':info_parroquia,
        #'mostrar_imagenes' : consulta_imagenes,
    })
#Bryan Sandoval implementacion de mapas de gogle para atractivos naturales *
def ver_ubicacion(request,id):
    valor = request.session.get('parroquia_id')
    info_parroquia=Parroquia.objects.filter(slug=valor)
    atrac_naturales=AtractivoNatural.objects.get(id=id)
    return render(request,'mapas/ver_ubicacion.html',{
     'mostrar_ubicacion':atrac_naturales,
     'mostrar_parroquia':info_parroquia,
    })
#******************************************************************

def atractivos_culturales(request):
    valor = request.session.get('parroquia_id')
    atrac_culturales=AtractivoCultural.objects.filter(parroquia__slug=valor)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    return render(request,'interfaz_turista/atrac_cultural.html',{
        'mostrar_atractivos':atrac_culturales,
        'mostrar_parroquia':info_parroquia,
    })

#redirigido por la agenda reenvia a la parroquia que le pertenece***************
def actividad_cultural(request,id):
    actividad_cultural=AtractivoCultural.objects.get(id=id)
    parroquia=Parroquia.objects.get(atractivocultural__id=id)
    request.session['parroquia_id']=parroquia.slug
    valor = request.session.get('parroquia_id')
    #para poder volver a reutilizar la consulta hago la consulta con filter
    info_parroquia=Parroquia.objects.filter(slug=valor)
    productos=Producto.objects.filter(empresa__tipo_id__parroquia__slug=valor)[:7]
    return render(request,'interfaz_turista/actividad_cultural.html',{
        'actividad_cultural':actividad_cultural,
        'mostrar_productos':productos,
        'mostrar_parroquia':info_parroquia,
    })

#Bryan Sandoval implementacion de mapas de gogle para atractivos Culturales *
def ver_ubicacion2(request,id):
    valor = request.session.get('parroquia_id')
    info_parroquia=Parroquia.objects.filter(slug=valor)
    atrac_cultural=AtractivoCultural.objects.get(id=id)
    return render(request,'mapas/ver_ubicacion.html',{
     'mostrar_ubicacion':atrac_cultural,
     'mostrar_parroquia':info_parroquia,
    })
#******************************************************************
def alojamientos(request):
    valor = request.session.get('parroquia_id')
    consulta_alojamientos=Alojamiento.objects.filter(parroquia__slug=valor)
    #print(consulta_alojamientos)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    return render(request,'interfaz_turista/alojamientos.html',{
        'mostrar_alojamientos':consulta_alojamientos,
        'mostrar_parroquia':info_parroquia,
    })
#Bryan Sandoval implementacion de mapas de gogle para alojamiento *
def ver_ubicacion3(request,id):
    valor = request.session.get('parroquia_id')
    info_parroquia=Parroquia.objects.filter(slug=valor)
    alojamiento=Alojamiento.objects.get(id=id)
    return render(request,'mapas/ver_ubicacion.html',{
     'mostrar_ubicacion':alojamiento,
     'mostrar_parroquia':info_parroquia,
    })
#******************************************************************
def restaurantes(request):
    valor = request.session.get('parroquia_id')
    consulta_restaurantes=Restaurante.objects.filter(parroquia__slug=valor)
    #print(consulta_restaurantes)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    return render(request,'interfaz_turista/restaurantes.html',{
        'mostrar_restaurantes':consulta_restaurantes,
        'mostrar_parroquia':info_parroquia,
    })
#Bryan Sandoval implementacion de mapas de gogle para restaurantes *
def ver_ubicacion4(request,id):
    valor = request.session.get('parroquia_id')
    info_parroquia=Parroquia.objects.filter(slug=valor)
    restaurante=Restaurante.objects.get(id=id)
    return render(request,'mapas/ver_ubicacion.html',{
     'mostrar_ubicacion':restaurante,
     'mostrar_parroquia':info_parroquia,
    })
#******************************************************************
#class FomentoProdutivo(TemplateView):
#    template_name = 'interfaz_turista/fomento_productivo.html'

def fomento_productivo(request):
    valor = request.session.get('parroquia_id')
    consulta_categorias=TipoEmp.objects.filter(parroquia__slug=valor)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    productos=Producto.objects.filter(empresa__tipo_id__parroquia__slug=valor)[:7]
    #print(consulta_categorias)
    return render(request,'interfaz_turista/fomento_productivo.html',{
        'mostrar_categorias':consulta_categorias,
        'mostrar_productos':productos,
        'mostrar_parroquia':info_parroquia,
    })
#mostrar empresas
def empresas(request, id):
    valor = request.session.get('parroquia_id')
    consulta_empresas=Empresa.objects.filter(tipo_id__id=id)
    parroquia=Parroquia.objects.get(slug=valor)
    #print(parroquia)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    return render(request,'interfaz_turista/empresas.html',{
        'mostrar_empresas':consulta_empresas,
        'parroquia':parroquia,
        'mostrar_parroquia':info_parroquia,
    })
#Bryan Sandoval implementacion de mapas de gogle para empresas *
def ubicacion_empresa(request,id):
    valor = request.session.get('parroquia_id')
    info_parroquia=Parroquia.objects.filter(slug=valor)
    empresa=Empresa.objects.get(id=id)
    return render(request,'mapas/ver_ubicacion.html',{
     'mostrar_ubicacion':empresa,
     'mostrar_parroquia':info_parroquia,
    })
#******************************************************************
def productos(request, id):
    #las productos que permetecen a la empresa seleccionada y ya que la empresa
    #esta ligada a la parroquia y a la categoria no hay problema
    valor = request.session.get('parroquia_id')
    consulta_productos=Producto.objects.filter(empresa__id=id)
    #print(consulta_productos)
    parroquia=Parroquia.objects.get(slug=valor)
    info_parroquia=Parroquia.objects.filter(slug=valor)
    empresa = Empresa.objects.get(id=id)
    return render(request,'interfaz_turista/productos.html',{
        'mostrar_productos':consulta_productos,
        'empresa':empresa,
        'mostrar_parroquia':info_parroquia,
    })
#Magaly Sarco implementacion de calendar *
def actividades(request):
    productos=Producto.objects.all()[:7]
    actividades_culturales=AtractivoCultural.objects.all()
    info_parroquia=Parroquia.objects.all()
    #print(actividades_culturales)
    return render(request,'interfaz_turista/actividades.html',{
        'mostrar_actividades_culturales':actividades_culturales,
        'listado_parroquias':info_parroquia,
        'mostrar_productos':productos,
    })

#Bryan Sandoval implementacion de mapas de gogle para atractivos naturales *
def ubicacion_parroquia(request):
    valor = request.session.get('parroquia_id')
    info_parroquia=Parroquia.objects.filter(slug=valor)
    parroquia=Parroquia.objects.get(slug=valor)
    atractivos_naturales=AtractivoCultural.objects.all()
    atractivos_culturales=AtractivoNatural.objects.all()
    return render(request,'mapas/ver_ubicacion.html',{
     'mostrar_ubicacion':parroquia,
     'mostrar_parroquia':info_parroquia,
    })
#******************************************************************

class ImagenesAtrNatural(ListView):
    model = ImagenesAtractivoNatural
    template_name = 'interfaz_turista/img_atr_natural.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_atractivos = ImagenesAtractivoNatural.objects.all().count()
        context['count'] = total_atractivos
        return context

#Bryan Sandoval mapa turistico *
def mapa_turistico(request):
    productos=Producto.objects.all()[:7]
    info_parroquia=Parroquia.objects.all()
    naturales=AtractivoNatural.objects.all()
    culturales=AtractivoCultural.objects.all()
    return render(request,'mapas/mapa_turistico.html',{
        'mostrar_productos':productos,
        'listado_parroquias':info_parroquia,
        'atractivos_naturales':naturales,
        'atractivos_culturales':culturales,
    })
