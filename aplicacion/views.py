from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def contacto(request):
    return render(request,'contacto.html')

def cursos(request):
    return render(request,'cursos.html')

def edicionproductos(request):
    return render(request,'edicionproductos.html')

def editarusuario(request):
    return render(request,'editarusuario.html')

def faqs(request):
    return render(request,'faqs.html')

def formpago(request):
    return render(request,'formpago.html')

def horas(request):
    return render(request,'horas.html')

def inicioSesionEstud(request):
    return render(request,'inicioSesionEstud.html')

def interfaz_de_compra(request):
    return render(request,'interfaz_de_compra.html')

def miscompras(request):
    return render(request,'miscompras.html')

def perfil(request):
    return render(request,'perfil.html')

def perfilAdmin(request):
    return render(request,'perfilAdmin.html')

def profesores(request):
    return render(request,'profesores.html')

def ventas(request):
    return render(request,'ventas.html')












# Create your views here.
