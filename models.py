from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    nombres = models.CharField(max_length=200)
    ap_paterno = models.CharField(max_length=200)
    ap_materno = models.CharField(max_length=200)

class Proveedor(models.Model):
    ID_PROVEEDOR = models.AutoField(primary_key=True)
    RUT_PROVEEDOR = models.CharField(max_length=200)
    NOMBRE_PROVEEDOR = models.CharField(max_length=200)
    TELEFONO_PROVEEDOR = models.CharField(max_length=200)
    DIRECCION = models.CharField(max_length=200)


class CATEGORIA(models.Model): #desmarcar
    ID_CATEGORIA = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)

class Producto(models.Model): #crear los nuevos 
    ID_PRODUCTO = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100)
    precio = models.IntegerField(default=100)


class CarritoDetalle(models.Model):
    id_carritoDetalle = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100)
    precio = models.IntegerField(default=100)
    cantidad = models.IntegerField(default=100)
    total = models.IntegerField(default=100)

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100)
    precio = models.IntegerField(default=100)
    cantidad = models.IntegerField(default=100)
    total = models.IntegerField(default=100)

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
    fecha_venta = models.TimeField(auto_now=False, auto_now_add=False)
    total_venta = models.IntegerField(default=100)
    boleta =  models.ForeignKey(Boleta, on_delete=models.PROTECT)

class BoletaDetalle(models.Model):
    id_boletadetalle = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100)
    precio = models.IntegerField(default=100)
    cantidad = models.IntegerField(default=100)
    total = models.IntegerField(default=100)

class Marca(models.Model):
    ID_MARCA = models.AutoField(primary_key=True)
    nombreMarca = models.CharField(max_length=100)

class Empleado(models.Model):
    ID_EMPLEADO = models.AutoField(primary_key=True)
    RUT_EMPLEADO = models.CharField(max_length=200)
    NOMBRE_EMPLEADO = models.CharField(max_length=200)
    APELLIDO_EMPLEADO = models.CharField(max_length=200)
    TELEFONO_EMPLEADO = models.CharField(max_length=200)
    DIRECCION = models.CharField(max_length=200)

class Contador(models.Model):
    id_contador= models.AutoField(primary_key=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.PROTECT)
    year = models.TimeField(auto_now=False, auto_now_add=False)
    mes = models.TimeField(auto_now=False, auto_now_add=False)

class Bodega(models.Model):
    ID_BODEGA = models.AutoField(primary_key=True)
    DIRECCION = models.CharField(max_length=200)
    STOCK = models.IntegerField(default=100)

class BodegaDetalle(models.Model):
    id_bodegaDetalle = models.AutoField(primary_key=True)
    bodega =  models.ForeignKey(Bodega, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=100)


class Cliente(models.Model):
    ID_CLIENTE = models.AutoField(primary_key=True)
    RUT_CLIENTE = models.CharField(max_length=200)
    NOMBRE_CLIENTE = models.CharField(max_length=200)
    APELLIDO_CLIENTE = models.CharField(max_length=200)
    TELEFONO_CLIENTE = models.CharField(max_length=200)
    DIRECCION_CLIENTE = models.CharField(max_length=200)

class Modelo(models.Model):
    ID_MODELO = models.AutoField(primary_key=True)
    NOMBRE_MODELO = models.CharField(max_length=100)
    