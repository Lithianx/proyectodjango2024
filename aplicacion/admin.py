from django.contrib import admin
from .models import Producto




class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso')
    list_filter = ('cursos',)
    search_fields = ('nombre', 'descripcion')

    fieldsets = (
        (None, {
            'fields': ('nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso')
        }),
    )

    


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso')
    list_filter = ('cursos',)
    search_fields = ('nombre', 'descripcion')

    fieldsets = (
        (None, {
            'fields': ('nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso')
        }),
    )

    



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cursos', 'cupos', 'descripcion', 'imagen_curso')
    list_filter = ('cursos',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

    actions = ['make_discount']

    





admin.site.register(Producto, ProductoAdmin)
