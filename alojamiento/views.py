from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from alojamiento.forms import FormularioAlojamientos
from alojamiento.models import Alojamiento
from parroquias.models import Parroquia

#-----MAGALY -> DECORADOR-------------------
from usuario.decorators import dispatch_decorator
from django.utils.decorators import method_decorator

class ListarAlojamiento(ListView):
    model = Alojamiento
    template_name = 'alojamiento/listar_alojamientos.html' #queryset = libro.objects.all()  objectList
    def get_queryset(self):
        return Alojamiento.objects.filter(parroquia__id=self.get_object()).order_by('nombre')

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
            return super(ListarAlojamiento, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

#class RegistrarAlojamiento(CreateView):
#    model = Alojamiento
#    form_class = FormularioAlojamientos
#    template_name = 'alojamiento/crear_alojamiento.html'
#    success_url = reverse_lazy('alojamiento:listar_alojamientos')

def registrarAlojamiento(request):
    #adquiero de la session el id de la parroquia donde el administrador es
    #el usuario que inicio secion
    valor = request.session.get('pk_parroquia')
    print(valor)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioAlojamientos(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('alojamiento:listar_alojamientos')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioAlojamientos({
                'parroquia':valor
            })
        return render(request,'alojamiento/crear_alojamiento.html',{
        #context
            'form':form
        })
    else:
        return redirect('index')

class ActualizarAlojamiento(UpdateView):
    model = Alojamiento
    template_name = 'alojamiento/crear_alojamiento.html'
    form_class = FormularioAlojamientos
    success_url = reverse_lazy('alojamiento:listar_alojamientos')

#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ActualizarAlojamiento, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
#eliminar usuarios
class EliminarAlojamiento(DeleteView):
    model = Alojamiento
    success_url = reverse_lazy('alojamiento:listar_alojamientos')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarAlojamiento, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
