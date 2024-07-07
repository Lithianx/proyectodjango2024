from django.contrib import messages  
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from aplicacion.forms import ComprarCursoForm, PagoForm,RegistroForm,form_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from aplicacion.models import CarritoItem, Compra, DetalleCompra, Perfil, Producto



def base(request):
    return render(request, 'Autoescuela/base.html')

def index(request):
    return render(request, 'Autoescuela/index.html')

def contacto(request):
    return render(request, 'Autoescuela/contacto.html')

def cursos(request):
    cursos = Producto.objects.all()
    comprar_curso_form = ComprarCursoForm()
    return render(request, 'Autoescuela/cursos.html', {'cursos': cursos, 'comprar_curso_form': comprar_curso_form})

def edicionproductos(request):
    return render(request, 'Autoescuela/edicionproductos.html')

def editarusuario(request):
    return render(request, 'Autoescuela/editarusuario.html')

def faqs(request):
    return render(request, 'Autoescuela/faqs.html')

def formpago(request):
    items_carrito = CarritoItem.objects.all()
    total = sum(item.producto.precio for item in items_carrito)  # Calcula el total del carrito

    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            perfil = request.user if request.user.is_authenticated else None

            # Crea la instancia de Compra
            compra = Compra(
                nombre_curso=form.cleaned_data['nombre'],  # Ajusta según tus necesidades
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
    return render(request, 'Autoescuela/horas.html')

def inicioSesionEstud(request):
    return render(request, 'Autoescuela/inicioSesionEstud.html')

def interfaz_de_compra(request):
    return render(request, 'Autoescuela/interfaz_de_compra.html')

def miscompras(request):
    compras = Compra.objects.filter(perfil=request.user)
    return render(request, 'Autoescuela/miscompras.html', {'compras': compras})

def perfil(request):
    return render(request, 'Autoescuela/perfil.html')

def perfilAdmin(request):
    return render(request, 'Autoescuela/perfilAdmin.html')

def profesores(request):
    return render(request, 'Autoescuela/profesores.html')

def ventas(request):
    return render(request, 'Autoescuela/ventas.html')

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
            return redirect('index')
    else:
        form = RegistroForm()
    
    return render(request, 'Autoescuela/form_registrarse.html', {'form': form})


@login_required
def carrito(request):
    
    
    items_carrito = CarritoItem.objects.all()
    

    total = sum(item.total_price for item in items_carrito)
    return render(request, 'Autoescuela/carrito.html', {'items_carrito': items_carrito, 'total': total, 'perfil': perfil})



def form_inicio_sesion(request):
    if request.method == 'POST':
        form = form_login(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = form_login()
    return render(request, 'login.html', {'form': form})


@login_required
def eliminar_carrito(request, producto_id):
    curso = get_object_or_404(Producto, id=producto_id)  # Ajustar el modelo
    curso.delete()
    messages.success(request, 'Curso eliminado')  # Ajustar el mensaje
    return redirect('carrito')


@login_required
def agregar_al_carrito(request, producto_id):
    if request.method == 'POST':
        form = ComprarCursoForm(request.POST)
        if form.is_valid():
            producto_id = form.cleaned_data['producto_id']
            producto = get_object_or_404(Producto, id=producto_id)
            carrito_item, created = CarritoItem.objects.get_or_create(producto=producto, compra=None, defaults={'cantidad': 1})

            if not created:
                carrito_item.cantidad += 1
                carrito_item.save()

            return redirect('carrito')
    return redirect('cursos')

# @login_required
# def ver_carrito(request):
#     compra = Compra.objects.filter(perfil=request.user, estado='Pendiente').first()
#     carrito_items = CarritoItem.objects.filter(compra=compra)
    
#     total = sum(item.producto.precio for item in carrito_items)  # Ajustar cálculo de total_price
    
#     datos = {
#         'carrito': carrito_items,
#         'total': total
#     }
#     return render(request, 'Autoescuela/carrito.html', datos)


@login_required
def quitar_del_carrito(request, producto_id):
    item = get_object_or_404(CarritoItem, id=producto_id, compra=None)
    item.delete()
    return redirect(request,'carrito')

@login_required
def proceder_a_compra(request):
    carrito_items = CarritoItem.objects.filter(compra=None, usuario=request.user)  # Añadido usuario
    if carrito_items.exists():
        compra = Compra.objects.create(perfil=request.user, precio=sum(item.producto.precio for item in carrito_items), estado='Pendiente')
        carrito_items.update(compra=compra)
        return redirect('formpago')
    return redirect('ver_carrito')

def pagoexitoso(request):
    return render(request, 'Autoescuela/pagoexitoso.html')

def listar_cursos(request):
    cursos = Producto.objects.all()
    return render(request, 'Autoescuela/cursos.html', {'cursos': cursos})



def navbar_context(request):
    usuario_autenticado = request.user.is_authenticated
    tiene_compras = False

    if usuario_autenticado:
        try:
            perfil = Perfil.objects.get(usuario=request.user)
            items_carrito = CarritoItem.objects.filter(compra__perfil=perfil, compra=None)
            tiene_compras = items_carrito.exists()
        except Perfil.DoesNotExist:
            pass

    return {
        'usuario_autenticado': usuario_autenticado,
        'tiene_compras': tiene_compras,
    }


































# from pyexpat.errors import messages
# from django.shortcuts import redirect, render, get_object_or_404
# from django.contrib.auth import login, authenticate, logout
# from aplicacion.forms import ComprarCursoForm, RegistroForm, form_login, PagoForm
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from aplicacion.models import CarritoItem, Compra, Perfil, DetalleCompra,Producto





# def base(request):
#     return render(request,'Autoescuela/base.html')

# def index(request):
#     return render(request, 'Autoescuela/index.html')

# def contacto(request):
#     return render(request,'Autoescuela/contacto.html')

# def cursos(request):
#     cursos = Producto.objects.all()
#     comprar_curso_form = ComprarCursoForm()
#     return render(request, 'Autoescuela/cursos.html', {'cursos': cursos, 'comprar_curso_form': comprar_curso_form})

# def edicionproductos(request):
#     return render(request,'Autoescuela/edicionproductos.html')

# def editarusuario(request):
#     return render(request,'Autoescuela/editarusuario.html')

# def faqs(request):
#     return render(request,'Autoescuela/faqs.html')

# def formpago(request):
#     items_carrito = CarritoItem.objects.all()
#     total = sum(item.producto.precio for item in items_carrito)  # Calcula el total del carrito

#     if request.method == 'POST':
#         form = PagoForm(request.POST)
#         if form.is_valid():
#             perfil = request.user if request.user.is_authenticated else None

#             # Crea la instancia de Compra
#             compra = Compra(
#                 nombre_curso=form.cleaned_data['nombre_Curso'],  # Ajusta según tus necesidades
#                 precio=total,
#                 estado='Pendiente',
#                 perfil=perfil
#             )
#             compra.save()

#             # Crea las instancias de DetalleCompra
#             for item in items_carrito:
#                 detalle_compra = DetalleCompra(
#                     compra=compra,
#                     producto=item.producto,
#                 )
#                 detalle_compra.save()

#             # Vacía el carrito después de realizar la compra
#             items_carrito.delete()

#             return redirect('index')
#     else:
#         form = PagoForm()

#     return render(request, 'Autoescuela/formpago.html', {'form': form, 'total': total})
# def horas(request):
#     return render(request,'Autoescuela/horas.html')

# def inicioSesionEstud(request):
#     return render(request,'Autoescuela/inicioSesionEstud.html')

# def interfaz_de_compra(request):
#     return render(request,'Autoescuela/interfaz_de_compra.html')

# def miscompras(request):
#     compras = Compra.objects.filter(perfil=request.user)
#     return render(request,'Autoescuela/miscompras.html', {'compras': compras})

# def perfil(request):
#     return render(request,'Autoescuela/perfil.html')

# def perfilAdmin(request):
#     return render(request,'Autoescuela/perfilAdmin.html')

# def profesores(request):
#     return render(request,'Autoescuela/profesores.html')

# def ventas(request):
#     return render(request,'Autoescuela/ventas.html')

# def form_registrarse(request):
#     return render(request,'Autoescuela/form_registrarse.html')


# @login_required
# def carrito(request):
#     items_carrito = CarritoItem.objects.filter(compra=None)
#     total = sum(item.producto.precio for item in items_carrito)
#     return render(request, 'Autoescuela/carrito.html', {'items_carrito': items_carrito, 'total': total})


# def form_inicio_sesion(request):
#     if request.method == 'POST':
#         form = form_login(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = form_login()
#     return render(request, 'Autoescuela/form_inicio_sesion.html', {'formulario': form})


# def form_registrarse(request):
#     if request.method == 'POST':
#         form = RegistroForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#             )
#             perfil = form.save(commit=False)
#             perfil.usuario = user
#             perfil.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = RegistroForm()
    
#     return render(request, 'Autoescuela/form_registrarse.html', {'form': form})
    


# @login_required
# def eliminar_carrito(request, producto_id):
#     curso = get_object_or_404(producto_id, id=producto_id) 
#     curso.delete()
#     messages.success(request, print('Curso eliminado'))
#     return redirect('cursos')






# @login_required
# def agregar_al_carrito(request, producto_id):
#     producto = get_object_or_404(Producto, id=producto_id)
#     carrito_item, created = CarritoItem.objects.get_or_create(producto=producto, compra=None, defaults={'cantidad': 1})
    
#     if not created:
#         carrito_item.cantidad += 1
#         carrito_item.save()
    
#     # Redirige al usuario al carrito después de agregar un curso
#     return redirect(request , 'carrito')

# @login_required
# def ver_carrito(request):
#     compra = Compra.objects.filter(perfil=request.user, estado='Pendiente').first()
#     carrito_items = CarritoItem.objects.filter(compra=compra)
    
#     total = sum(item.total_price for item in carrito_items)
    
#     datos = {
#         'carrito': carrito_items,
#         'total': total
#     }
#     return render(request, 'carrito.html', datos)


# @login_required
# def quitar_del_carrito(request, producto_id):
#     item = get_object_or_404(CarritoItem, id=producto_id, compra=None)
#     item.delete()
#     return redirect(request,'carrito')

# @login_required
# def proceder_a_compra(request):
#     carrito_items = CarritoItem.objects.filter(compra=None)
#     if carrito_items.exists():
#         compra = Compra.objects.create(perfil=request.user, precio=sum(item.total_price for item in carrito_items), estado='Pendiente')
#         carrito_items.update(compra=compra)
#         return redirect('pago')
#     return redirect('ver_carrito')

# def pagoexitoso(request):
#     return render(request, 'Autoescuela/pagoexitoso.html')


# def listar_cursos(request):
#     cursos = Producto.objects.all()  
#     return render(request, 'cursos.html', {'cursos': cursos})

# # Create your views here.
