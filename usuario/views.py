from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from usuario.forms import FormularioLogin,FormularioUsuario,FormularioEditarUsuario,FormularioEditarPasswordUsuario
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
#crud
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from usuario.models import Usuario
from parroquias.models import Parroquia


from django.utils.decorators import method_decorator
from .decorators import dispatch_decorator

#iniciar secion
class Login(FormView):
    template_name = 'usuario/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')
    # medidas de seguridad
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs): #verifica la peticion
        #si hay un usuario q hace una peticion y esta logeado.
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url()) #redireccina
        else:
            return super(Login, self).dispatch(request, *args, **kwargs) #si o esta logeado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parroquias = Parroquia.objects.all()
        context['listado_parroquias'] = parroquias
        return context
    #valida el formulario de esta vista

    def form_valid(self, form):
        login(self.request, form.get_user()) #indico qe cree una iinstancia e inicie una secion
        return super(Login, self).form_valid(form)

#cerrar secion
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

#listar usuarios registrados en el perfil del administrador
class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuario/listar_usuario.html'
    #para listar puedo usar esta forma o
    #queryset = Usuario.objects.filter(usuario_activo = True)  #listar los usuarios activos
    #o definiendo los get_queryset filtre por usuarios turistas
    def get_queryset(self):
        # filtro para que no se listen los usuarios superadmin y los administradores parroquiales
        return self.model.objects.filter(usuario_admin=False).filter(is_superuser=False)

#-----------------------------------------------------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ListadoUsuario, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

#funciones con las que cada usuario realiza acciones con su informacion de perfil.
#registrar usuarios
class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parroquias = Parroquia.objects.all()
        context['listado_parroquias'] = parroquias
        return context

class MisDatos(ListView):
    model = Usuario
    template_name = 'usuario/mis_datos.html'
    def get_queryset(self):
        obtener_email=self.request.user.email
        return Usuario.objects.filter(email=obtener_email)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parroquias = Parroquia.objects.all()
        context['listado_parroquias'] = parroquias
        return context

class ActualizarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuario/crear_usuario.html'
    form_class = FormularioEditarUsuario
    success_url = reverse_lazy('mis_datos')


class ActualizarPasswordUsuario(UpdateView):
    model = Usuario
    template_name = 'usuario/crear_usuario.html'
    form_class = FormularioEditarPasswordUsuario
    success_url = reverse_lazy('mis_datos')

class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('index')

#Borrar usuarios registrados desde el perfil del administrador
class AdminEliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')
