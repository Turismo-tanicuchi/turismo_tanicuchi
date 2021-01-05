from django import forms
from usuario.models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from parroquias.models import Parroquia
# tipos de atractivos.
from atractivos_naturales.models import TipoAN
from atractivos_culturales.models import TipoAC

class FormularioUsuario(forms.ModelForm):
    #si quiro un campo extra lo puedo definir aqui
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            #componentes para html
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('first_name','last_name','email','direccion','usuario_admin')
        labels = {
            'first_name': 'Ingrese sus nombres',
            'last_name':'Ingrese sus apellidos',
            'email':'Ingrese su email',
            'direccion':'Ingrese su dirección',
            'usuario_admin': 'Marque si el usuario registrado sera un administrador parroquial',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombres',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellidos',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su direccion',
                }
            ),
            'usuario_admin': forms.CheckboxInput(
                attrs = {
                    'placeholder': 'Es administrador',
                }
            )
        }

        #validar contraseña
    def clean_password2(self):
        """ Validación de Contraseña
        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.
        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        # cleaned al hacer click en el boton de registrar llega a django se guarda y se valida
        # los campos a validar se pasan por un diccionario que ya esta limpia
        password2 = self.cleaned_data.get('password2')

#--------------------------- MAGALY--------------------------------------------------------------------
        if len(password1)<8:
            raise forms.ValidationError('Contraseña incorrecta, debe contener almenos 8 digitos')
        else:
            if password1 != password2:
                raise forms.ValidationError('Contraseñas no coinciden!')
            return password2
        return password1

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name.isdigit():
            raise forms.ValidationError('El campo "Nombres" no puede ser numerico')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name.isdigit():
            raise forms.ValidationError('El campo "Apellidos" no puede ser numerico')
        return last_name
#------------------------------------------------------------------------------------------------------

    #metodo save() guardar los datos
    def save(self,commit = True):
        user = super().save(commit = False) #si commit es false guarda una instancia
        user.set_password(self.cleaned_data['password1']) #encripta contraseña
        if commit:
            user.save()
        return user

class FormularioEditarUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('first_name','last_name','email','direccion','usuario_admin')
        labels = {
            'first_name': 'Ingrese sus nombres',
            'last_name':'Ingrese sus apellidos',
            'email':'Ingrese su email',
            'direccion':'Ingrese su dirección',
            'usuario_admin': 'Marque si el usuario registrado sera un administrador parroquial',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombres',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellidos',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su direccion',
                }
            ),
            'usuario_admin': forms.CheckboxInput(
                attrs = {
                    'placeholder': 'Es administrador',
                }
            )
        }
#--------------------------- MAGALY--------------------------------------------------------------------
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name.isdigit():
            raise forms.ValidationError('El campo "Nombres" no puede ser numerico')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name.isdigit():
            raise forms.ValidationError('El campo "Apellidos" no puede ser numerico')
        return last_name

class FormularioParroquia(forms.ModelForm):

    class Meta:
        model = Parroquia
        fields = ('nombre_parr','direccion','email','telefono','administrador')
        labels = {
            #como quiero que se vean los labels
            'nombre_parr': 'Nombre de la Parroquia',
            'direccion':'Dirección',
            'email': 'Ingrese el correo parroquial',
            'telefono': 'Ingrese el Teléfono de la parroquia',
            'administrador': 'Selecciona al administrador de esta parróquia',
        }
        widgets = {
            'nombre_parr': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la parroquia',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                }
            ),
            'administrador': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                }
            ),
        }

class Formulario_tipo_natural(forms.ModelForm):
    class Meta:
        model = TipoAN
        fields = ('nombre_tipo_an','descripcion')
        labels = {
            #como quiero que se vean los labels
            'nombre_tipo_an': 'Nombre del tipo de atractivo',
            'descripcion':'Descripción del tipo de atractivo (Opcional)',
        }
        widgets = {
            'nombre_tipo_an': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Tipo de atractivo',
                }
            ),
            'descripcion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }

class Formulario_tipo_cultural(forms.ModelForm):
    class Meta:
        model = TipoAC
        fields = ('nombre_tipo_ac','descripcion')
        labels = {
            #como quiero que se vean los labels
            'nombre_tipo_ac': 'Nombre del tipo de atractivo',
            'descripcion':'Descripción del tipo de atractivo (Opcional)',
        }
        widgets = {
            'nombre_tipo_ac': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Tipo de atractivo',
                }
            ),
            'descripcion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }
