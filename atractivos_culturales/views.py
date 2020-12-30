from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from atractivos_culturales.forms import FormularioAtractivoCultural
from atractivos_culturales.models import AtractivoCultural
from parroquias.models import Parroquia
from django.contrib import messages

#-----MAGALY -> DECORADOR-------------------
from usuario.decorators import dispatch_decorator
from django.utils.decorators import method_decorator

class ListarAtractivoCultural(ListView):
    model = AtractivoCultural
    template_name = 'atractivos_culturales/listar_atractivos.html'
    def get_queryset(self):
        return AtractivoCultural.objects.filter(parroquia__id=self.get_object()).order_by('nombre')

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self, queryset=None):
        parroquia= Parroquia.objects.get(administrador__id=self.request.user.id)
        return parroquia.id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ListarAtractivoCultural, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

# vista basada en clases.
#class RegistrarAtractivoCultural(CreateView):
#    model = AtractivoCultural
#    form_class = FormularioAtractivoCultural
#    template_name = 'atractivos_culturales/crear_atractivo.html'
#    success_url = reverse_lazy('atractivos_culturales:listado_atractivos')


def registrarAtractivoCultural(request):
    #adquiero de la session el id de la parroquia donde el administrador es
    #el usuario que inicio secion
    valor = request.session.get('pk_parroquia')
    print(valor)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioAtractivoCultural(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('atractivos_culturales:listado_atractivos')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioAtractivoCultural({
                'parroquia':valor
            })
        return render(request,'atractivos_culturales/crear_atractivo.html',{
        #context
            'form':form
        })
    else:
        return redirect('index')

class ActualizarAtractivoCultural(UpdateView):
    model = AtractivoCultural
    template_name = 'atractivos_culturales/crear_atractivo.html'
    form_class = FormularioAtractivoCultural
    success_url = reverse_lazy('atractivos_culturales:listado_atractivos')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ActualizarAtractivoCultural, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
#eliminar usuarios
class EliminarAtractivoCultural(DeleteView):
    model = AtractivoCultural
    success_url = reverse_lazy('atractivos_culturales:listado_atractivos')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarAtractivoCultural, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
