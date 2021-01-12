from django import forms
from .models import AtractivoNatural
from parroquias.models import Parroquia

class FormularioAtractivoNatural(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = AtractivoNatural
        fields = ('nombre','descripcion','direccion','latitud','longitud','imagen','tipo_id','parroquia')
        labels = {
            'nombre': 'Nombre del Atractivo Natural',
            'descripcion':'Descripción',
            'direccion':'Direccion',
            'latitud': 'coordenadas Latitud',
            'longitud':'coordenadas Longitud',
            'imagen': 'Imagen',
            'tipo_id': 'Elija el tipo',
            'parroquia': 'Elige la parroquia'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'nombre del atractivo',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la direccion',
                }
            ),
            'latitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'latitud',
                }
            ),
            'longitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'longitud',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'tipo_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo',
                }
            ),
            'parroquia': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la parroquia',
                    #que no se pueda cambiar
                    'readonly':'readonly',
                    #que no se vea
                    'type':'hidden'
                }
            )
        }
#--------------------------- MAGALY--------------------------------------------------------------------
    def clean_latitud(self):
        latitud = self.cleaned_data.get('latitud')
        if str(latitud).isalpha():
            raise forms.ValidationError('El campo "Latitud" no puede ser alfabético"')
        else:
            for i in range(len(str(latitud))):
                if str(latitud)[i].isspace():
                    raise forms.ValidationError('El campo no puede tener espacios en blanco')
        return latitud

    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
        if str(longitud).isalpha():
            raise forms.ValidationError('El campo "Longitud" no puede ser alfabético"')
        else:
            for i in range(len(str(longitud))):
                if str(longitud)[i].isspace():
                    raise forms.ValidationError('El campo no puede tener espacios en blanco')    
        return longitud
#------------------------------------------------------------------------------------------------------
