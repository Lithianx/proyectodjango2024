from django import forms
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from aplicacion.models import Compra, Cursos, Perfil, Producto



class form_login(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 



class RegistroAdminForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    nombre_estudiante = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rut = forms.CharField(
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    foto_perfil = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    rol = forms.ChoiceField(
        choices=[('Administrador', 'Administrador'), ('Estudiante', 'Estudiante')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cursos = forms.ChoiceField(
        choices=Cursos,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'nombre_estudiante', 'rut', 'direccion', 'foto_perfil', 'rol', 'cursos']

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
    rut = forms.CharField(label='RUT', max_length=12, widget=forms.TextInput(attrs={'class': 'form-control rut', 'placeholder': '12345678-9'}))
    direccion_envio = forms.CharField(label='Dirección de Envío', max_length=255)
    metodo_pago = forms.ChoiceField(label='Método de Pago', choices=[('credito', 'Tarjeta de Crédito'), ('debito', 'Tarjeta de Débito')])
    nombre_titular = forms.CharField(label='Nombre del Titular', max_length=100)
    numero_tarjeta = forms.CharField(label='Número de Tarjeta', max_length=19, widget=forms.TextInput(attrs={'class': 'form-control numero-tarjeta', 'placeholder': 'XXXX-XXXX-XXXX-XXXX'}))
    fecha_expiracion = forms.CharField(label='Vencimiento', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control fecha-expiracion', 'placeholder': 'MM/YY'}))
    cvv = forms.CharField(label='CVV', max_length=3)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        if not nombre.isalpha():
            raise forms.ValidationError('El nombre debe contener solo letras')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if len(apellido) < 3:
            raise forms.ValidationError('El apellido debe tener al menos 3 caracteres')
        if not apellido.isalpha():
            raise forms.ValidationError('El apellido debe contener solo letras')
        return apellido

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut = rut.replace('.', '').replace(' ', '')
        if len(rut) < 8:
            raise forms.ValidationError('El RUT debe tener al menos 8 caracteres')
        if '-' not in rut or rut.count('-') > 1:
            raise forms.ValidationError('RUT inválido')
        rut_number, verificador = rut.split('-')
        if not (rut_number.isdigit() and (verificador.isdigit() or verificador.lower() == 'k')):
            raise forms.ValidationError('RUT inválido')
        suma = 0
        factor = 2
        rut_number = int(rut_number)
        while rut_number > 0:
            suma += (rut_number % 10) * factor
            rut_number //= 10
            factor = factor % 7 + 1
        resto = suma % 11
        dv_calculado = 11 - resto if resto != 1 else 0
        if dv_calculado == 10:
            dv_calculado = 'k'
        return rut

    def clean_direccion_envio(self):
        direccion_envio = self.cleaned_data['direccion_envio']
        if len(direccion_envio) < 5:
            raise forms.ValidationError('La dirección de envío debe tener al menos 5 caracteres')
        return direccion_envio

    def clean_nombre_titular(self):
        nombre_titular = self.cleaned_data['nombre_titular']
        if len(nombre_titular) < 3:
            raise forms.ValidationError('El nombre del titular debe tener al menos 3 caracteres')
        if not nombre_titular.isalpha():
            raise forms.ValidationError('El nombre del titular debe contener solo letras')
        return nombre_titular

    def clean_numero_tarjeta(self):
        numero_tarjeta = self.cleaned_data['numero_tarjeta']
        numero_tarjeta = numero_tarjeta.replace('-', '')
        def luhn_algorithm(n):
            r = [int(ch) for ch in str(n)][::-1]
            return sum(r[0::2] + [sum(divmod(d*2, 10)) for d in r[1::2]]) % 10 == 0
        if len(numero_tarjeta) < 16:
            raise forms.ValidationError('El número de tarjeta debe tener al menos 16 caracteres')
        if not numero_tarjeta.isdigit():
            raise forms.ValidationError('El número de tarjeta debe contener solo números')
        else:
            if not luhn_algorithm(numero_tarjeta):
                raise forms.ValidationError('Número de tarjeta inválido')
        return numero_tarjeta

    def clean_fecha_expiracion(self):
        fecha_expiracion = self.cleaned_data['fecha_expiracion']
        if not fecha_expiracion:
            raise forms.ValidationError('La fecha de expiración es requerida.')
        if '/' not in fecha_expiracion:
            raise forms.ValidationError('El formato de la fecha de expiración debe ser MM/YY.')
        try:
            month, year = fecha_expiracion.split('/')
        except ValueError:
            raise forms.ValidationError('Formato de fecha de expiración inválido.')
        if not (1 <= int(month) <= 12):
            raise forms.ValidationError('Mes inválido')
        if int(year) < 23:
            raise forms.ValidationError('Año inválido')
        return fecha_expiracion

    def clean_cvv(self):
        cvv = self.cleaned_data['cvv']
        if len(cvv) < 3:
            raise forms.ValidationError('El CVV debe tener al menos 3 caracteres')
        if not cvv.isdigit():
            raise forms.ValidationError('El CVV debe contener solo números')
        return cvv
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre_estudiante','correo', 'direccion' , 'foto_perfil' ]


class ComprarCursoForm(forms.Form):
    producto_id = forms.IntegerField(widget=forms.HiddenInput)
    def clean_producto_id(self):
        producto_id = self.cleaned_data['producto_id']
        if not isinstance(producto_id, int) or producto_id <= 0:
            raise forms.ValidationError('ID de producto inválido')
        return producto_id



#SECCION CRUD
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre_estudiante', 'rut', 'correo', 'cursos', 'direccion', 'foto_perfil', 'rol']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso']



class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['nombre_curso', 'precio', 'estado', 'perfil']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['perfil'].queryset = User.objects.filter(is_superuser=False)


    
