from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from superadministracion.forms import FormularioUsuario,FormularioEditarUsuario,FormularioParroquia
from django.urls import reverse_lazy
from usuario.models import Usuario
from usuario.forms import FormularioEditarPasswordUsuario
from parroquias.models import Parroquia
from django.contrib import messages
# tipos de atractivos.
from atractivos_naturales.models import TipoAN
from atractivos_culturales.models import TipoAC
from superadministracion.forms import Formulario_tipo_natural,Formulario_tipo_cultural

def home_superadmin(request):
    return render(request,'superadministracion/superadmin.html',{
    #context
    })

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'superadministracion/todos_usuarios.html'
    def get_queryset(self):
        # filtro para que no se listen los usuarios superadmin
        return self.model.objects.filter(is_superuser=False)

class CrearUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'superadministracion/crear_nuevousuario.html'
    success_url = reverse_lazy('superadministracion:mostrar_usuarios')

class ActualizarUsuario(UpdateView):
    model = Usuario
    template_name = 'superadministracion/crear_nuevousuario.html'
    form_class = FormularioEditarUsuario
    success_url = reverse_lazy('superadministracion:mostrar_usuarios')

class ActualizarPasswordUsuario(UpdateView):
    model = Usuario
    template_name = 'superadministracion/crear_nuevousuario.html'
    form_class = FormularioEditarPasswordUsuario
    success_url = reverse_lazy('superadministracion:mostrar_usuarios')
#eliminar usuarios
class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'superadministracion/eliminar_usuario.html'
    success_url = reverse_lazy('superadministracion:mostrar_usuarios')

class MostrarParroquias(ListView):
    model = Parroquia
    template_name = 'superadministracion/mostrar_parroquia.html'
    queryset = Parroquia.objects.all().order_by('nombre_parr')

def registrar_parroquia(request):
    usuarios = Usuario.objects.filter(usuario_admin=True).order_by('email')
    if request.user.is_superuser == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioParroquia(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('superadministracion:mostrar_parroquias')
            else:
                messages.success(request,'No se pudo crear el registro')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioParroquia({
            })
        return render(request,'superadministracion/crear_parroquia.html',{
        #context
            'mostrar_usuarios':usuarios,
            'form':form
        })
    else:
        return redirect('index')

def actualizarparroquia(request,id):
    usuarios = Usuario.objects.filter(usuario_admin=True).order_by('email')
    # Recuperamos la instancia del producto
    parroquia = Parroquia.objects.get(id=id)
    # comprobamos si es get o Post
    if request.user.is_superuser == True:
        if request.method == 'GET':
            form = FormularioParroquia(instance=parroquia)
        else:
            form = FormularioParroquia(request.POST,request.FILES, instance = parroquia)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('superadministracion:mostrar_parroquias')
        return render(request,'superadministracion/crear_parroquia.html',{
        #context
            'mostrar_usuarios':usuarios,
            'ver_parroquia':parroquia,
            'form':form
        })
    else:
        return redirect('index')

class EliminarParroquia(DeleteView):
    model = Parroquia
    template_name = 'superadministracion/eliminar_parroquia.html'
    success_url = reverse_lazy('superadministracion:mostrar_parroquias')

# tipos de atractivos naturales
class MostrarTiposNaturales(ListView):
    model = TipoAN
    template_name = 'superadministracion/mostrar_tipo.html'
    queryset = TipoAN.objects.all().order_by('nombre_tipo_an')

class CrearTipoNatural(CreateView):
    model = TipoAN
    form_class = Formulario_tipo_natural
    template_name = 'superadministracion/crear_tipoN.html'
    success_url = reverse_lazy('superadministracion:mostrar_tipo_Natural')

class ActualizarTipoNatural(UpdateView):
    model = TipoAN
    template_name = 'superadministracion/crear_tipoN.html'
    form_class = Formulario_tipo_natural
    success_url = reverse_lazy('superadministracion:mostrar_tipo_Natural')

class EliminarTipoNatural(DeleteView):
    model = TipoAN
    template_name = 'superadministracion/eliminar_tipoN.html'
    success_url = reverse_lazy('superadministracion:mostrar_tipo_Natural')

# tipos de atractivos culturales
class MostrarTiposCulturales(ListView):
    model = TipoAC
    template_name = 'superadministracion/mostrar_tipoC.html'
    queryset = TipoAC.objects.all().order_by('nombre_tipo_ac')

class CrearTipoCultural(CreateView):
    model = TipoAC
    form_class = Formulario_tipo_cultural
    template_name = 'superadministracion/crear_tipoN.html'
    success_url = reverse_lazy('superadministracion:mostrar_tipo_cultural')

class ActualizarTipoCultural(UpdateView):
    model = TipoAC
    template_name = 'superadministracion/crear_tipoN.html'
    form_class = Formulario_tipo_cultural
    success_url = reverse_lazy('superadministracion:mostrar_tipo_cultural')

class EliminarTipoCultural(DeleteView):
    model = TipoAC
    template_name = 'superadministracion/eliminar_tipoC.html'
    success_url = reverse_lazy('superadministracion:mostrar_tipo_cultural')
