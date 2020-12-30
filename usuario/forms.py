from django import forms
from usuario.models import Usuario
from django.contrib.auth.forms import AuthenticationForm

#crear form de login
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        # esta es una manera de darle clases a los campos
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
    """ Formulario de Registro de un Usuario en la base de datos
    Variables:
        - password1:    Contraseña
        - password2:    Verificación de la contraseña
    """
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
        fields = ('first_name','last_name','email','direccion','imagen')
        labels = {
            'first_name': 'Ingrese sus nombres',
            'last_name':'Ingrese sus apellidos',
            'email':'Ingrese su email',
            'direccion':'Ingrese su dirección',
            'imagen': 'Cargue una imagen para su perfil',
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
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
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
        fields = ('first_name','last_name','email','direccion','imagen')
        labels = {
            'first_name': 'Ingrese sus nombres',
            'last_name':'Ingrese sus apellidos',
            'email':'Ingrese su email',
            'direccion':'Ingrese su dirección',
            'imagen': 'Cargue una imagen para su perfil',
        }
        widgets = {
            'fisrt_name': forms.TextInput(
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
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
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
#------------------------------------------------------------------------------------------------------

class FormularioEditarPasswordUsuario(forms.ModelForm):
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
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
        fields = ()
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
#--------------------------- MAGALY--------------------------------------------------------------------
        if len(password1)<8:
            raise forms.ValidationError('Contraseña incorrecta, debe contener almenos 8 digitos')
        else:
            if password1 != password2:
                raise forms.ValidationError('Contraseñas no coinciden!')
            return password2
        return password1
#------------------------------------------------------------------------------------------------------

    def save(self,commit = True):
        user = super().save(commit = False) #si commit es false guarda una instancia
        user.set_password(self.cleaned_data['password1']) #encripta contraseña
        if commit:
            user.save()
        return user
