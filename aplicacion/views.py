from django.contrib import messages  
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from aplicacion.forms import CompraForm, ComprarCursoForm, EditarPerfilForm, PagoForm, PerfilForm, ProductoForm, RegistroAdminForm,RegistroForm,form_login
from aplicacion.forms import ComprarCursoForm, EditarPerfilForm, PagoForm,RegistroForm,form_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from aplicacion.models import CarritoItem, Compra, DetalleCompra, Perfil, Producto


def es_superuser(user):
    return user.is_superuser

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
            if request.user.is_authenticated:
                perfil = request.user
            else:
                perfil = None

            # Verificar si el usuario ya compró alguno de los cursos en el carrito
            for item in items_carrito:
                if Compra.objects.filter(perfil=perfil, detalles__producto=item.producto).exists():
                    messages.error(request, f'Ya compraste el curso {item.producto.nombre}.')
                    return redirect('carrito')

            # Crea la instancia de Compra
            compra = Compra.objects.create(
                nombre_curso=form.cleaned_data['nombre'],  # Ajusta según tus necesidades
                precio=total,
                estado='Proceso',
                perfil=perfil
            )

            # Crea las instancias de DetalleCompra asociadas a la compra
            for item in items_carrito:
                compra.detalles.create(
                    producto=item.producto,
                )

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
    compras = Compra.objects.filter(perfil=request.user).order_by('fecha_pedido')
    compras_con_id_local = [(idx + 1, compra) for idx, compra in enumerate(compras)]
    return render(request, 'Autoescuela/miscompras.html', {'compras_con_id_local': compras_con_id_local})


def perfil(request):
    # Asegurándonos de que se obtiene el perfil correcto del usuario
    usuario = Perfil.objects.get(usuario=request.user)

    if request.method == 'POST':
        # Instanciar el formulario con los datos POST y archivos, además del perfil existente
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()  # Guardamos los cambios en el perfil
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('perfil')
    else:
        # Instanciar el formulario con el perfil existente
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'Autoescuela/perfil.html', {'usuario': usuario, 'form': form})


    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()  # Guardamos los cambios en el perfil
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'Autoescuela/perfil.html', {'usuario': usuario, 'form': form})


# def perfilAdmin(request):
#     return render(request, 'Autoescuela/perfilAdmin.html')

def profesores(request):
    return render(request, 'Autoescuela/profesores.html')

def confirmar_eliminacion(request):
    return render(request, 'Autoescuela/profesores.html')

def ventas(request):
    return render(request, 'Autoescuela/confirmar_eliminacion.html')

def form_registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            print(f"Username: {username}, Email: {email}, Password: {password}")
            
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            
            print(f"User saved: {user}")
            
            user = authenticate(request, username=username, password=password)
            print(f"Authenticated user: {user}")
            
            if user is not None:
                login(request, user)
                
                perfil = Perfil.objects.create(usuario=user, correo=email, rol='Estudiante', nombre_estudiante=username)
                perfil.save()
                
                messages.success(request, 'Registro exitoso.')
                return redirect('login')
            else:
                messages.error(request, 'Error al autenticar el usuario.')
                print("Authentication failed.")
        else:
            messages.error(request, 'Formulario no válido. Corrige los errores indicados.')
            print("Formulario no válido.")
    else:
        form = RegistroForm()
    
    return render(request, 'Autoescuela/form_registrarse.html', {'form': form})





@login_required
def carrito(request):
    items_carrito = CarritoItem.objects.filter(compra=None)
    total = sum(item.total_price for item in items_carrito)
    tiene_items = items_carrito.exists()  # Verifica si hay items en el carrito

    return render(request, 'Autoescuela/carrito.html', {
        'items_carrito': items_carrito,
        'total': total,
        'tiene_items': tiene_items,  # Pasa esta variable al contexto del template
    })


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
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Verificar si el usuario ya compró este curso
    if Compra.objects.filter(perfil=request.user, detalles__producto=producto).exists():
        messages.error(request, 'Ya has comprado este curso.')
        return redirect('cursos')
    
    # Verificar si el curso ya está en el carrito
    if CarritoItem.objects.filter(producto=producto, compra=None).exists():
        messages.error(request, 'Este curso ya está en tu carrito.')
        return redirect('cursos')
    
    # Si no existe, agregar el curso al carrito
    carrito_item, created = CarritoItem.objects.get_or_create(
        producto=producto, compra=None, defaults={'cantidad': 1}
    )
    
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()

    messages.success(request, 'Curso agregado al carrito.')
    return redirect('carrito')





@login_required
def quitar_del_carrito(request, producto_id):
    item = get_object_or_404(CarritoItem, id=producto_id, compra=None)
    item.delete()
    return redirect('carrito')

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
            perfil =request.user
            items_carrito = CarritoItem.objects.filter(compra__perfil=perfil, compra=None)
            tiene_compras = items_carrito.exists()
        except Perfil.DoesNotExist:
            pass

    return {
        'usuario_autenticado': usuario_autenticado,
        'tiene_compras': tiene_compras,
    }

def cerrar_sesion(request):
    CarritoItem.objects.all().delete()
    logout(request)
    return redirect('index')



#seccion CRUD


# def editar_producto_form(request):
#     return render(request,'Autoescuela/editar_producto_form.html')


@login_required
def editar_producto_form(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('PerfilAdmin')
        else:
            messages.error(request, 'Formulario no válido. Corrige los errores indicados.')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Autoescuela/editar_producto_form.html', {'form': form})



@login_required
def listar_productos(request):
    productos = Producto.objects.all()  
    return render(request, 'Autoescuela/perfilAdmin.html', {'productos': productos}) 


@login_required
def editar_perfil_form(request, id):
    perfil = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            print()
            form.save()
            return redirect('perfilAdmin')  
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'Autoescuela/editar_perfil_form.html', {'form': form})



@login_required
def editar_compra_form(request, id):
    compra = get_object_or_404(Compra, pk=id)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra actualizada exitosamente.')
            return redirect('perfilAdmin')  
        else:
            messages.error(request, 'Formulario no válido. Corrige los errores indicados.')
    else:
        form = CompraForm(instance=compra)
    
    return render(request, 'Autoescuela/editar_compra_form.html', {'form': form})



def confirmar_eliminacion_compra(request):
    return render(request,'Autoescuela/confirmar_eliminacion_compra.html')

def confirmar_eliminacion_perfil(request):
    return render(request,'Autoescuela/confirmar_eliminacion_perfil.html')

def confirmar_eliminacion_producto(request):
    return render(request,'Autoescuela/confirmar_eliminacion_producto.html')



@user_passes_test(es_superuser)
@login_required
def perfilAdmin(request):
    compras = Compra.objects.all()
    usuarios = User.objects.all()
    productos = Producto.objects.all()
    return render(request, 'Autoescuela/perfilAdmin.html', {'compras': compras, 'usuarios': usuarios,'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('perfilAdmin')
    else:
        form = ProductoForm()
    return render(request, 'Autoescuela/editar_producto_form.html', {'form': form})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('perfilAdmin')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Autoescuela/editar_producto_form.html', {'form': form})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('perfilAdmin')
    return render(request, 'Autoescuela/confirmar_eliminacion_producto.html', {'obj': producto})

@login_required
def crear_perfil(request):
    if request.method == 'POST':
        form = RegistroAdminForm(request.POST, request.FILES)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()

            perfil = Perfil.objects.create(
                usuario=user,
                nombre_estudiante=form.cleaned_data['nombre_estudiante'],
                rut=form.cleaned_data['rut'],
                correo=form.cleaned_data['email'],
                direccion=form.cleaned_data['direccion'],
                foto_perfil=form.cleaned_data['foto_perfil'],
                rol=form.cleaned_data['rol'],
                cursos=form.cleaned_data['cursos']
            )
            perfil.save()

            messages.success(request, 'Perfil creado exitosamente.')
            return redirect('perfilAdmin')  # Ajusta esta URL según sea necesario
        else:
            messages.error(request, 'Formulario no válido. Corrige los errores indicados.')
    else:
        form = RegistroAdminForm()

    return render(request, 'Autoescuela/editar_perfil_form.html', {'form': form})


@login_required
def editar_perfil(request, id):
    perfil = get_object_or_404(User, pk=id)
    
    print(perfil)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfilAdmin')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'Autoescuela/editar_perfil_form.html', {'form': form})

@login_required
def eliminar_perfil(request, id):
    perfil = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        perfil.delete()
        return redirect('perfilAdmin')
    return render(request, 'Autoescuela/confirmar_eliminacion_perfil.html', {'perfil': perfil})


@login_required
def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.save()
            messages.success(request, 'Compra creada exitosamente.')
            return redirect('perfilAdmin')  
        else:
            messages.error(request, 'Formulario no válido. Corrige los errores indicados.')
    else:
        form = CompraForm()

    return render(request, 'Autoescuela/crear_compra.html', {'form': form})

@login_required
def editar_compra(request, id):
    compra = get_object_or_404(Compra, pk=id)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('perfilAdmin')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'Autoescuela/editar_compra_form.html', {'form': form})

@login_required
def eliminar_compra(request, id):
    compra = get_object_or_404(Compra, pk=id)
    if request.method == 'POST':
        compra.delete()
        return redirect('perfilAdmin')
    return render(request, 'Autoescuela/confirmar_eliminacion_compra.html', {'compra': compra})

#pass test



