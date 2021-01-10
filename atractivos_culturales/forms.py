from django import forms
from .models import AtractivoCultural

class FormularioAtractivoCultural(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = AtractivoCultural
        fields = ('nombre','descripcion','direccion','latitud','longitud','imagen','tipo_id','fecha','parroquia')
        labels = {
            #como quiero que se vena los labels
            'nombre': 'Nombre del Atractivo Cultural',
            'descripcion':'Descripción',
            'direccion':'Dirección',
            'latitud': 'Coordenadas Latitud',
            'longitud':'Coordenadas Longitud',
            'imagen': 'Imagen',
            'tipo': 'Elija el tipo',
            'fecha': 'Engrese la fecha si se trata de una festividad (año-mes-dia ejm 2021-11-20)',
            'parroquia': 'Elige la parroquia'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del atractivo',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
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
            'fecha': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'seleccine la fecha si se trata de una festividad',
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
            raise forms.ValidationError('El campo "Latitud" es obligatorio y no puede ser alfabetico"')
        return latitud

    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
        if str(longitud).isalpha():
            raise forms.ValidationError('El campo "Longitud" es obligatorio y no puede ser alfabetico"')
        return longitud
#------------------------------------------------------------------------------------------------------
