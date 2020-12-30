from django.shortcuts import redirect
from .models import Usuario

def dispatch_decorator(function):
    def wrap(request, *args, **kwargs):
        if request.user.usuario_admin == True:
            return function(request, *args, **kwargs)
        else:
            return redirect('index')
    return wrap
