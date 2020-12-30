from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from transporte.forms import FormularioTransporte
from transporte.models import Transporte
from parroquias.models import Parroquia

#-----MAGALY -> DECORADOR-------------------
from usuario.decorators import dispatch_decorator
from django.utils.decorators import method_decorator

class ListarTransporte(ListView):
    model = Transporte
    template_name = 'transporte/listar_transporte.html'

    def get_queryset(self):
        return Transporte.objects.filter(parroquia__id=self.get_object()).order_by('nombre')

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
            return super(ListarTransporte, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

# Create your views here.
#class RegistrarTransporte(CreateView):
#    model = Transporte
#    form_class = FormularioTransporte
#    template_name = 'transporte/crear_transporte.html'
#    success_url = reverse_lazy('transporte:listado_transporte')

def registrarTransporte(request):
    #adquiero de la session el id de la parroquia donde el administrador es
    #el usuario que inicio secion
    valor = request.session.get('pk_parroquia')
    print(valor)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioTransporte(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('transporte:listado_transporte')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioTransporte({
                'parroquia':valor
            })
        return render(request,'transporte/crear_transporte.html',{
        #context
            'form':form
        })
    else:
        return redirect('index')

class ActualizarTransporte(UpdateView):
    model = Transporte
    template_name = 'transporte/crear_transporte.html'
    form_class = FormularioTransporte
    success_url = reverse_lazy('transporte:listado_transporte')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ActualizarTransporte, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
#eliminar usuarios
class EliminarTransporte(DeleteView):
    model = Transporte
    success_url = reverse_lazy('transporte:listado_transporte')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarTransporte, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
