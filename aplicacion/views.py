from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from aplicacion.forms import RegistroForm, form_login, PagoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from aplicacion.models import CarritoItem, Compra, Perfil, DetalleCompra




def base(request):
    return render(request,'Autoescuela/base.html')

def index(request):
    return render(request, 'Autoescuela/index.html')

def contacto(request):
    return render(request,'Autoescuela/contacto.html')

def cursos(request):
    return render(request,'Autoescuela/cursos.html')

def edicionproductos(request):
    return render(request,'Autoescuela/edicionproductos.html')

def editarusuario(request):
    return render(request,'Autoescuela/editarusuario.html')

def faqs(request):
    return render(request,'Autoescuela/faqs.html')

def formpago(request):
    items_carrito = CarritoItem.objects.all()
    total = sum(item.producto.precio for item in items_carrito)  # Calcula el total del carrito

    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            perfil = request.user if request.user.is_authenticated else None

            # Crea la instancia de Compra
            compra = Compra(
                nombre_curso=form.cleaned_data['nombre_Curso'],  # Ajusta según tus necesidades
                precio=total,
                estado='Pendiente',
                perfil=perfil
            )
            compra.save()

            # Crea las instancias de DetalleCompra
            for item in items_carrito:
                detalle_compra = DetalleCompra(
                    compra=compra,
                    producto=item.producto,
                )
                detalle_compra.save()

            # Vacía el carrito después de realizar la compra
            items_carrito.delete()

            return redirect('index')
    else:
        form = PagoForm()

    return render(request, 'Autoescuela/formpago.html', {'form': form, 'total': total})
def horas(request):
    return render(request,'Autoescuela/horas.html')

def inicioSesionEstud(request):
    return render(request,'Autoescuela/inicioSesionEstud.html')

def interfaz_de_compra(request):
    return render(request,'Autoescuela/interfaz_de_compra.html')

def miscompras(request):
    compras = Compra.objects.filter(perfil=request.user)
    return render(request,'Autoescuela/miscompras.html', {'compras': compras})

def perfil(request):
    return render(request,'Autoescuela/perfil.html')

def perfilAdmin(request):
    return render(request,'Autoescuela/perfilAdmin.html')

def profesores(request):
    return render(request,'Autoescuela/profesores.html')

def ventas(request):
    return render(request,'Autoescuela/ventas.html')

def form_registrarse(request):
    return render(request,'Autoescuela/form_registrarse.html')

def form_inicio_sesion(request):
    if request.method == 'POST':
        form = form_login(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = form_login()
    return render(request, 'Autoescuela/form_inicio_sesion.html', {'formulario': form})


def form_registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            perfil = form.save(commit=False)
            perfil.usuario = user
            perfil.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    
    return render(request, 'Autoescuela/form_registrarse.html', {'form': form})


@login_required
def agregar_carrito(request, curso_id):
    curso = get_object_or_404(curso, id=curso_id) 

    messages.success(request, print('Curso Agregado'))
    return redirect('cursos')

@login_required
def eliminar_carrito(request, curso_id):
    curso = get_object_or_404(curso, id=curso_id) 
    curso.delete()
    messages.success(request, print('Curso eliminado'))
    return redirect('cursos')








# Create your views here.
