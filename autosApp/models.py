from django.db import models

# Create your models here.

class Sucursal(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    año = models.IntegerField()
    patente = models.CharField(max_length=255)
    nombre_vendedor = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places = 2)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

class Venta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    comprador_nombre = models.CharField(max_length=255)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
