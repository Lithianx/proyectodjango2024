from django.shortcuts import render


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












# Create your views here.
