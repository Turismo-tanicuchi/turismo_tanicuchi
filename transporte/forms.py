from django import forms
from transporte.models import Transporte

class FormularioTransporte(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Transporte
        fields = ('nombre','ruta','imagen','observaciones','parroquia')
        labels = {
            #como quiero que se vena los labels
            'nombre': 'Nombre de la cooperativa o línea',

            'ruta':'Ingrese El origen y destino',
            'imagen':'Cargue una imagen referente a la cooperativa o línea',
            'observaciones': 'Ingrese información adicional',
            'parroquia':'Eliga la parroquia'

        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la cooperativa o línea',
                }
            ),
            'tipo_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo',
                }
            ),
            'ruta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Origen y el destino',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'observaciones': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese información adicional que quiera registrar',
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
