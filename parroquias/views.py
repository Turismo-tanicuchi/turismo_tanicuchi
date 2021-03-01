from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import UpdateView,DeleteView,CreateView
from django.views.generic.detail import DetailView
from .models import Parroquia,ImagenesParroquia
from django.urls import reverse_lazy
from parroquias.forms import FormularioParroquia,FormularioImgParroquia

#-----MAGALY -> DECORADOR-------------------
from usuario.decorators import dispatch_decorator
from django.utils.decorators import method_decorator

# Create your views here.
class ParroquiasListView(ListView):
    template_name = 'parroquias/lista_parroquias.html'
    queryset = Parroquia.objects.all().order_by('nombre_parr')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message']='Listado de parroquias'
        context['parroquias'] = context['parroquia_list']
        #print('parroquia_list')
        return context

class ParroquiaDetailView(DetailView):
    model = Parroquia
    template_name = 'parroquias/parroquia.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        return context

class ParroquiaSearchListView(ListView):
    template_name='parroquias/search.html'
    def get_queryset(self):
        return Parroquia.objects.filter(nombre_parr__icontains=self.query())

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['parroquia_list'].count()
        return context

# mostrar datos en el administrador para que pueda editar

class MostrarDatosParroquia(ListView):
    model = Parroquia
    template_name = 'parroquias/mostrar_parroquia.html' #queryset = libro.objects.all()  objectList
    #queryset = Parroquia.objects.all().order_by('nombre_parr')
    def get_queryset(self):
        return Parroquia.objects.filter(administrador__id=self.get_object())

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user.id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MostrarImagenesParroquia(ListView):
    model = ImagenesParroquia
    template_name = 'parroquias/img_parroquia.html'
    #queryset = ImagenesParroquia.objects.filter(parroquia__id=1)
    def get_queryset(self):
        return ImagenesParroquia.objects.filter(parroquia__id=self.get_object())

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self, queryset=None):
        parroquia= Parroquia.objects.get(administrador__id=self.request.user.id)
        return parroquia.id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# regstro de imgparroquia con vista basada enclases
#class RegistrarImgParroquia(CreateView):
#    model = ImagenesParroquia
#    form_class = FormularioImgParroquia
#    template_name = 'Parroquias/crear_imagen.html'
#    success_url = reverse_lazy('parroquias:img_parroquia')

def registrarImagenes(request):
    #adquiero de la session el id de la parroquia donde el administrador es
    #el usuario que inicio secion
    valor = request.session.get('pk_parroquia')
    print(valor)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioImgParroquia(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('parroquias:img_parroquia')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioImgParroquia({
                'parroquia':valor
            })
        return render(request,'parroquias/crear_imagen.html',{
        #context
            'form':form
        })
    else:
        return redirect('index')

class EliminarImagenesParroquia(DeleteView):
    model = ImagenesParroquia
    success_url = reverse_lazy('parroquias:img_parroquia')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarImagenesParroquia, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

class ActualizarDatosParroquia(UpdateView):
    model = Parroquia
    template_name = 'Parroquias/crear_parroquia.html'
    form_class = FormularioParroquia
    success_url = reverse_lazy('parroquias:datos_parroquia')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ActualizarDatosParroquia, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
