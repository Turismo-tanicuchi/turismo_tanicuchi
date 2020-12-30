from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from restaurante.forms import FormularioRestaurante
from restaurante.models import Restaurante
from parroquias.models import Parroquia

#-----MAGALY -> DECORADOR-------------------
from usuario.decorators import dispatch_decorator
from django.utils.decorators import method_decorator

class ListarRestaurante(ListView):
    model = Restaurante
    template_name = 'restaurante/listar_restaurantes.html' #queryset = libro.objects.all()  objectList
    def get_queryset(self):
        return Restaurante.objects.filter(parroquia__id=self.get_object()).order_by('nombre')

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
            return super(ListarRestaurante, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
#class RegistrarRestaurante(CreateView):
#    model = Restaurante
#    form_class = FormularioRestaurante
#    template_name = 'restaurante/crear_restaurante.html'
#    success_url = reverse_lazy('restaurante:listar_restaurantes')

def registrarRestaurante(request):
    #adquiero de la session el id de la parroquia donde el administrador es
    #el usuario que inicio secion
    valor = request.session.get('pk_parroquia')
    print(valor)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioRestaurante(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('restaurante:listar_restaurantes')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioRestaurante({
                'parroquia':valor
            })
        return render(request,'restaurante/crear_restaurante.html',{
        #context
            'form':form
        })
    else:
        return redirect('index')

class ActualizarRestaurante(UpdateView):
    model = Restaurante
    template_name = 'restaurante/crear_restaurante.html'
    form_class = FormularioRestaurante
    success_url = reverse_lazy('restaurante:listar_restaurantes')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ActualizarRestaurante, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

class EliminarRestaurante(DeleteView):
    model = Restaurante
    success_url = reverse_lazy('restaurante:listar_restaurantes')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarRestaurante, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
