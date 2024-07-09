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

from aplicacion.views import *   

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
    path('form_registrarse/', form_registrarse , name='form_registrarse'),
    path('carrito/', carrito , name='carrito'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar_del_carrito/<int:producto_id>/', quitar_del_carrito, name='quitar_del_carrito'),
    path('pagoexitoso/', pagoexitoso, name='pagoexitoso'),
    path('cerrarSesion/', cerrar_sesion, name='cerrarSesion'),
    

    #SECCION CRUD
    

    path('editar_producto_form/<int:id>/', editar_producto_form, name='editar_producto_form'),
    path('editar_perfil_form/<int:id>/', editar_perfil_form, name='editar_perfil_form'),
    path('editar_compra_form/<int:id>/', editar_compra_form, name='editar_compra_form'),
    path('confirmar_eliminacion_compra/<int:id>/', confirmar_eliminacion_compra, name='confirmar_eliminacion_compra'),
    path('confirmar_eliminacion_perfil/<int:id>/', confirmar_eliminacion_perfil, name='confirmar_eliminacion_perfil'),

    path('crear_producto/', crear_producto, name='crear_producto'),
    path('listar_productos/<int:id>', listar_productos, name='listar_productos'),
    path('editar_producto/<int:id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('crear_perfil/', crear_perfil, name='crear_perfil'),
    path('editar_perfil/<int:id>/', editar_perfil, name='editar_perfil'),
    path('eliminar_perfil/<int:id>/', eliminar_perfil, name='eliminar_perfil'),
    path('crear_compra/', crear_compra, name='crear_compra'),
    path('editar_compra/<int:id>/', editar_compra, name='editar_compra'),
    path('eliminar_compra/<int:id>/', eliminar_compra, name='eliminar_compra'),
    

    

    



]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urls del sitio