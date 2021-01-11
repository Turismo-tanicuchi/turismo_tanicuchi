from django.shortcuts import render
from parroquias.models import Parroquia
from empresa.models import Producto
from superadministracion.models import InformacionTurismo
#para el administrador
def home_view(request):
    user = request.user.id if request.user.is_authenticated else None
    parroquia=Parroquia.objects.get(administrador__id=user)
    request.session['pk_parroquia']=parroquia.id #almacenamos en secion el pk de la parroquia
    valor = request.session.get('pk_parroquia')
    #print(valor)
    return render(request,'base_admin.html',{
    #context
    })
#para el turista
def index_view(request):
    parroquias=Parroquia.objects.all()
    informacion=InformacionTurismo.objects.all()
    #print(parroquias)
    print(informacion)
    return render(request,'index.html',{
    #context lista de parroquias
    'listado_parroquias':parroquias,
    'informacion_pagina':informacion,
    })
