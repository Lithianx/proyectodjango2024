from django import forms
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from aplicacion.models import Perfil



class form_login(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class RegistroForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Perfil
        fields = ['nombre_estudiante', 'rut', 'correo', 'cursos', 'direccion', 'foto_perfil', 'rol']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'cursos': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data
class PagoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Correo Electrónico')
    rut = forms.CharField(label='RUT', max_length=10)
    direccion_envio = forms.CharField(label='Dirección de Envío', max_length=255)
    metodo_pago = forms.ChoiceField(label='Método de Pago', choices=[('credito', 'Tarjeta de Crédito'), ('debito', 'Tarjeta de Débito')])
    nombre_titular = forms.CharField(label='Nombre del Titular', max_length=100)
    numero_tarjeta = forms.CharField(label='Número de Tarjeta', max_length=16)
    vencimiento = forms.CharField(label='Vencimiento', max_length=5)
    cvv = forms.CharField(label='CVV', max_length=3)

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre_estudiante','correo', 'direccion' , 'foto_perfil' ]


class ComprarCursoForm(forms.Form):
    producto_id = forms.IntegerField(widget=forms.HiddenInput)