from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from empresa.forms import FormularioEmpresa,FormularioProducto,FormularioCategoriaEmpresa,FormularioEditProducto,FormularioEditEmpresa
from empresa.models import Empresa,Producto,TipoEmp
from parroquias.models import Parroquia
from django.contrib import messages

#-----MAGALY -> DECORADOR-------------------
from usuario.decorators import dispatch_decorator
from django.utils.decorators import method_decorator


#****************************categorias de empresas *****************
class ListarCategoriasEmpresa(ListView):
    model = TipoEmp
    template_name = 'empresa/listar_categorias_empresa.html'
    def get_queryset(self):
        return TipoEmp.objects.filter(parroquia__id=self.get_object()).order_by('nombre')

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
            return super(ListarCategoriasEmpresa, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

def registrarCategoriaEmpresa(request):
    valor = request.session.get('pk_parroquia')
    print(valor)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioCategoriaEmpresa(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('empresa:listado_categorias_empresa')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioCategoriaEmpresa({
                'parroquia':valor
            })
        return render(request,'empresa/crear_categoria.html',{
        #context
            'form':form
        })
    else:
        return redirect('index')

class ActualizarCategoriaEmpresa(UpdateView):
    model = TipoEmp
    template_name = 'empresa/crear_categoria.html'
    form_class = FormularioCategoriaEmpresa
    success_url = reverse_lazy('empresa:listado_categorias_empresa')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(ActualizarCategoriaEmpresa, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
#eliminar usuarios

class EliminarCategoriaEmpresa(DeleteView):
    model = TipoEmp
    success_url = reverse_lazy('empresa:listado_categorias_empresa')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarCategoriaEmpresa, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

#**************************** Empresas *****************

class ListarEmpresa(ListView):
    model = Empresa
    template_name = 'empresa/listar_empresa.html'
    def get_queryset(self):
        return Empresa.objects.filter(tipo_id__parroquia__id=self.get_object()).order_by('nombre')

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
            return super(ListarEmpresa, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

#class RegistrarEmpresa(CreateView):
#    model = Empresa
#    form_class = FormularioEmpresa
#    template_name = 'empresa/crear_empresa.html'
#    success_url = reverse_lazy('empresa:listado_empresa')

def registrarEmpresa(request):
    valor = request.session.get('pk_parroquia')
    print(valor)
    parroquia = Parroquia.objects.get(id=valor)
    print(parroquia)
    categorias = TipoEmp.objects.filter(parroquia__id=parroquia.id).order_by('nombre')
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioEmpresa(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('empresa:listado_empresa')
            else:
                messages.success(request,'no se pudo')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioEmpresa({
            })
        return render(request,'empresa/crear_empresa.html',{
        #context
            'mostrar_categoria':categorias,
            'form':form
        })
    else:
        return redirect('index')
#class ActualizarEmpresa(UpdateView):
#    model = Empresa
#    template_name = 'empresa/crear_empresa.html'
#    form_class = FormularioEmpresa
#    success_url = reverse_lazy('empresa:listado_empresa')

def actualizarEmpresa(request,id):
    valor = request.session.get('pk_parroquia')
    categorias = TipoEmp.objects.filter(parroquia__id=valor).order_by('nombre')
    # Recuperamos la instancia del producto
    empresa = Empresa.objects.get(id=id)
    # comprobamos si es get o Post
    if request.user.usuario_admin == True:
        if request.method == 'GET':
            form = FormularioEditEmpresa(instance=empresa)
        else:
            form = FormularioEditEmpresa(request.POST,request.FILES, instance = empresa)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('empresa:listado_empresa')
        return render(request,'empresa/editar_empresa.html',{
        #context
            'mostrar_categoria':categorias,
            'form':form
        })
    else:
        return redirect('index')

#eliminar usuarios
class EliminarEmpresa(DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa:listado_empresa')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarEmpresa, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------

#********************************productos****************************
class ListarProducto(ListView):
    model = Producto
    template_name = 'empresa/listar_producto.html'
    def get_queryset(self):
        return Producto.objects.filter(empresa__tipo_id__parroquia__id=self.get_object()).order_by('nombre')

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
            return super(ListarProducto, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
#class RegistrarProducto(CreateView):
#    model = Producto
#    form_class = FormularioProducto
#    template_name = 'empresa/crear_producto.html'
#    success_url = reverse_lazy('empresa:listado_producto')

def registrarProducto(request):
    valor = request.session.get('pk_parroquia')
    print(valor)
    parroquia = Parroquia.objects.get(id=valor)
    print(parroquia)
    empresa=Empresa.objects.filter(tipo_id__parroquia__id=parroquia.id).order_by('nombre')
    print(empresa)
    #si la peticion es por el metodo post
    if request.user.usuario_admin == True:
        if request.method =='POST':
            #obtener valores q envia el Formulario
            form = FormularioProducto(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('empresa:listado_producto')
        #si la peticion es por get mando por defecto el id de la parroquia
        else:
            form = FormularioProducto({
            })
        return render(request,'empresa/crear_producto.html',{
        #context
            'mostrar_empresas':empresa,
            'form':form
        })
    else:
        return redirect('index')

#class ActualizarProducto(UpdateView):
#    model = Producto
#    template_name = 'empresa/crear_producto.html'
#    form_class = FormularioProducto
#    success_url = reverse_lazy('empresa:listado_producto')

def actualizarProducto(request,id):
    valor = request.session.get('pk_parroquia')
    parroquia = Parroquia.objects.get(id=valor)
    print(parroquia)
    empresa=Empresa.objects.filter(tipo_id__parroquia__id=parroquia.id).order_by('nombre')
    print(empresa)
    # Recuperamos la instancia del producto
    producto = Producto.objects.get(id=id)
    print(producto.empresa)
    # comprobamos si es get o Post
    if request.user.usuario_admin == True:
        if request.method == 'GET':
            form = FormularioEditProducto(instance=producto)
        else:
            form = FormularioEditProducto(request.POST,request.FILES, instance = producto)
            if form.is_valid():
                form.save()
                messages.success(request,'Almacenado exitosamente')
                return redirect('empresa:listado_producto')

        return render(request,'empresa/editar_producto.html',{
        #context
            'mostrar_empresas':empresa,
            'mostrar_producto':producto,
            'form':form
        })
    else:
        return redirect('index')

#eliminar usuarios
class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('empresa:listado_producto')
#-------------------------MAGALY -> DECORADOR---------------------------------
    @method_decorator(dispatch_decorator)
    def dispatch(self, request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return super(EliminarProducto, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------------------------
