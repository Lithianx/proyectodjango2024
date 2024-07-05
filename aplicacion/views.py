from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from aplicacion.forms import RegistroForm, form_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from aplicacion.models import CarritoItem, Compra, Producto




def base(request):
    return render(request,'Autoescuela/base.html')

def index(request):
    return render(request, 'Autoescuela/index.html')

def contacto(request):
    return render(request,'Autoescuela/contacto.html')

def cursos(request):
    cursos = Producto.objects.all()
    return render(request,'Autoescuela/cursos.html', {'cursos': cursos})

def edicionproductos(request):
    return render(request,'Autoescuela/edicionproductos.html')

def editarusuario(request):
    return render(request,'Autoescuela/editarusuario.html')

def faqs(request):
    return render(request,'Autoescuela/faqs.html')

def formpago(request):
    return render(request,'Autoescuela/formpago.html')

def horas(request):
    return render(request,'Autoescuela/horas.html')

def inicioSesionEstud(request):
    return render(request,'Autoescuela/inicioSesionEstud.html')

def interfaz_de_compra(request):
    return render(request,'Autoescuela/interfaz_de_compra.html')

def miscompras(request):
    return render(request,'Autoescuela/miscompras.html')

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


def carrito(request):
    return render(request,'Autoescuela/carrito.html')

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
    
# @login_required
# def agregar_carrito(request, curso_id):
#     curso = get_object_or_404(curso, id=curso_id) 

#     messages.success(request, print('Curso Agregado'))
#     return redirect('cursos')

@login_required
def eliminar_carrito(request, curso_id):
    curso = get_object_or_404(curso, id=curso_id) 
    curso.delete()
    messages.success(request, print('Curso eliminado'))
    return redirect('cursos')


# def form_pago(request):
#     if request.method == 'POST':
#         form = form_pago(request.POST)
#         if form.is_valid():
#             # Procesar la información del formulario
#             # Puedes guardar los datos en la base de datos o hacer otras acciones necesarias
#             # Por simplicidad, solo redirigiremos a una página de éxito
#             return redirect('pago_exitoso')
#     else:
#         form = PagoForm()
    
#     return render(request, 'pago.html', {'form': form})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, created = CarritoItem.objects.get_or_create(producto=producto, compra=None, defaults={'cantidad': 1})
    
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito_items = CarritoItem.objects.filter(compra=None)
    total = sum(item.total_price for item in carrito_items)
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})

@login_required
def proceder_a_compra(request):
    carrito_items = CarritoItem.objects.filter(compra=None)
    if carrito_items.exists():
        compra = Compra.objects.create(perfil=request.user, precio=sum(item.total_price for item in carrito_items), estado='Pendiente')
        carrito_items.update(compra=compra)
        return redirect('pago')
    return redirect('ver_carrito')




def listar_cursos(request):
    cursos = Producto.objects.all()  
    return render(request, 'cursos.html', {'cursos': cursos})

# Create your views here.
