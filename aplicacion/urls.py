"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from aplicacion.views import contacto, cursos, edicionproductos, editarusuario, faqs, formpago, horas, index, inicioSesionEstud, interfaz_de_compra, miscompras, perfil, perfilAdmin, profesores, ventas

urlpatterns = [
    path('',index, name='index'),
    path('contacto/', contacto , name='contacto'),
    path('cursos/', cursos , name='cursos'),
    path('edicionproductos/', edicionproductos , name='edicionproductos'),
    path('editarusuario/', editarusuario , name='editarusuario'),
    path('faqs/', faqs , name='faqs'),
    path('formpago/', formpago , name='formpago'),
    path('horas/', horas , name='horas'),
    path('inicioSesionEstud/', inicioSesionEstud , name='inicioSesionEstud'),
    path('interfaz_de_compra/', interfaz_de_compra , name='interfaz_de_compra'),
    path('miscompras/', miscompras , name='miscompras'),
    path('perfil/', perfil , name='perfil'),
    path('perfilAdmin/', perfilAdmin , name='perfilAdmin'),
    path('profesores/', profesores , name='profesores'),
    path('ventas/', ventas , name='ventas'),
    



]


#urls del sitio