from django.contrib import admin
from .models import CarritoItem, Compra, DetalleCompra, Perfil, Producto

# Configuración del modelo Perfil
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre_estudiante', 'rut', 'correo', 'cursos', 'direccion', 'rol')
    search_fields = ('nombre_estudiante', 'rut', 'correo')
    list_filter = ('cursos', 'rol')

# Configuración del modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso')
    list_filter = ('cursos',)
    search_fields = ('nombre', 'descripcion')
    fieldsets = (
        (None, {
            'fields': ('nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso')
        }),
    )

# Configuración del modelo Compra
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_curso', 'fecha_pedido', 'precio', 'estado', 'perfil')
    search_fields = ('nombre_curso', 'perfil__usuario__username', 'perfil__nombre_estudiante')
    list_filter = ('estado', 'fecha_pedido')

# Configuración del modelo DetalleCompra
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto')
    search_fields = ('compra__id', 'producto__nombre')

# Configuración del modelo CarritoItem
class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('producto', 'compra')
    search_fields = ('producto__nombre', 'compra__id')

# Registro de modelos en el sitio de administración
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(DetalleCompra, DetalleCompraAdmin)
admin.site.register(CarritoItem, CarritoItemAdmin)

