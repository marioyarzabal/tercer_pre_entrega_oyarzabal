from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni=models.IntegerField()
    fecha_nacimiento= models.DateField()
    domicilio=models.CharField(max_length=300)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}"


class Proveedor(models.Model):
    id_proveedor=models.IntegerField()
    nombre = models.CharField(max_length=100)
    cuit=models.IntegerField()
    domicilio=models.CharField(max_length=300)
    email=models.EmailField()
    TIPO_PRODUCTO_CHOICES = [
        ('Medicamentos', 'Medicamentos'),
        ('Perfumeria', 'Perfumeria'),
        ('Regaleria', 'Regaleria'),
        ('Libreria', 'Libreria'),
        ('Descartables', 'Descartables'),
        ('Otros', 'Otros'),
    ]
    tipo_producto = models.CharField(max_length=100, choices=TIPO_PRODUCTO_CHOICES)
    #tipo_producto=models.CharField(max_length=100)
    limite_compra = models.DecimalField(max_digits=10, decimal_places=2) 
    status=models.BooleanField()

    class Meta:
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"

    def __str__(self):
        return f"{self.nombre}, {self.cuit}, {self.domicilio}"

class Producto(models.Model):
    id_producto=models.IntegerField()
    id_proveedor=models.IntegerField()
    nombre = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100)
    fecha_elav= models.DateField()
    fecha_vence= models.DateField()
    droga=models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre}, {self.presentacion}, {self.droga}, {self.precio}, {self.id_producto}"

class Stock(models.Model):
    id_producto=models.IntegerField()
    cantidad_unidades=models.IntegerField() #unidades en stock
    min_unidades=models.IntegerField() #Minimo de unidades para pedir reposicion

    def __str__(self):
        return f"{self.id_producto}, {self.cantidad_unidades}, {self.min_unidades}"

class Cuenta(models.Model):
    id_cliente=models.IntegerField()
    id_producto=models.IntegerField()
    cantidad_unidades=models.IntegerField()
    status=models.CharField(max_length=10)  #pagado/debe
    fecha_pago=models.DateField() 
    fecha_compra=models.DateField()
    
    def __str__(self):
        return f"{self.id_cliente}, {self.id_producto}, {self.cantidad_unidades}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   