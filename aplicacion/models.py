from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
Cursos = [
    ('Clase B', 'Clase B'),
    ('Clase A2', 'Clase A2'),
    ('Clase A3', 'Clase A3'),
]

class Perfil(models.Model): 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_estudiante = models.CharField(max_length=50, unique=True, verbose_name="Nombre de estudiante")
    rut = models.CharField(max_length=10, unique=True, verbose_name="RUT", blank=True, null=True)
    correo = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    cursos = models.CharField(max_length=20, choices=Cursos, verbose_name="Cursos")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    foto_perfil = models.ImageField(upload_to='usuarios/', blank=True, null=True, verbose_name="Foto de perfil")
    rol = models.CharField(max_length=20, choices=[('Administrador', 'Administrador'), ('Estudiante', 'Estudiante')], verbose_name="Rol")

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.correo}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del curso")
    precio = models.PositiveIntegerField( verbose_name="Precio")
    cursos = models.CharField(max_length=20, choices=Cursos, verbose_name="Cursos")
    descripcion = models.TextField(verbose_name="Descripción del curso")
    imagen_curso = models.ImageField(upload_to='cursos/', verbose_name="Imagen Curso")


    def __str__(self):
        return self.nombre

class Compra(models.Model):
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre del curso")
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de compra")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    estado = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')], verbose_name="Estado")
    perfil = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Perfil", null=True, blank=True)
    

    def __str__(self):
        return f"Compra #{self.id} - {self.perfil.nombre_curso} - {self.precio}"
    
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles')
    tipo_pago = models.CharField(max_length=30, choices=[('Credito', 'Credito'), ('Debito', 'Debito'), ('Transferencia', 'Transferencia')], verbose_name="Tipo de Pago")
    def __str__(self):
        return f"{self.producto.nombre} x {self.tipo_pago}"
    

class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.cantidad} of {self.producto.nombre}'

    @property
    def total_price(self):
        return self.cantidad * self.producto.precio