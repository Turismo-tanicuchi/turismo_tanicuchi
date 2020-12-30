from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from atractivos_naturales.forms import FormularioAtractivoNatural
from atractivos_naturales.models import AtractivoNatural
from parroquias.models import Parroquia

#-----MAGALY -> DECORADOR-------------------
from usuario.decorators import dispatch_decorator
from django.utils.decorators import method_decorator

#listado de atractivos naturales que pertenecen a la parroquia del administrador q inicio secion
class ListarAtractivoNatural(ListView):
    model = AtractivoNatural
    template_name = 'atractivos_naturales/listar_atractivos.html'
    #queryset = AtractivoNatural.objects.all().order_by('nombre') #obtener todas
    def get_queryset(self):
        return AtractivoNatural.objects.filter(parroquia__id=self.get_object()).order_by('nombre')

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
            return super(ListarAtractivoNatural, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

# regstro de imgparroquia con vista basada enclases
#class RegistrarAtractivoNatural(CreateView):
#    model = AtractivoNatural
#    form_class = FormularioAtractivoNatural
#    template_name = 'atractivos_naturales/crear_atractivo.html'
#    success_url = reverse_lazy('atractivos_naturales:listado_atractivos')

def registrarAtractivoNatural(request):
    #adquiero de la session el id de la parroquia donde el administrador es
    #el usuario que inicio secion
    valor = request.session.get('pk_parroquia')
    print(valor)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioAtractivoNatural(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('atractivos_naturales:listado_atractivos')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioAtractivoNatural({
                'parroquia':valor
            })
        return render(request,'atractivos_naturales/crear_atractivo.html',{
        #context
            'form':form
        })
    else:
        return redirect('index')

class ActualizarAtractivoNatural(UpdateView):
    model = AtractivoNatural
    template_name = 'atractivos_naturales/crear_atractivo.html'
    form_class = FormularioAtractivoNatural
    success_url = reverse_lazy('atractivos_naturales:listado_atractivos')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ActualizarAtractivoNatural, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

#eliminar usuarios
class EliminarAtractivoNatural(DeleteView):
    model = AtractivoNatural
    success_url = reverse_lazy('atractivos_naturales:listado_atractivos')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarAtractivoNatural, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
