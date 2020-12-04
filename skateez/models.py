import datetime

from django.utils import timezone

from django.urls import reverse

from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# --- INDEX ---

class IndexView(models.Model):
    template_name = 'skateez/index.html'

# --- Items ---

class Tabla(models.Model):
    nombre = models.CharField(max_length=30)
    medida = models.CharField(max_length=30)
    concavo = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
    Precio = models.CharField(max_length=20, default='0')
    Cantidad = models.IntegerField(default='0')
    disponible = models.BooleanField(null='false')
    pass
    class Meta:
      verbose_name_plural = "Tabla"
      ordering = ["-id"]
    def __str__(self):
       return self.nombre      
    


class Ejes(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    altura = models.CharField(max_length=10)
    modelo = models.CharField(max_length=5)
    color = models.CharField(max_length=10)
    Precio = models.CharField(max_length=20, default='0')
    Cantidad = models.IntegerField( default='0')
    disponible = models.BooleanField(null='false')  
    pass
    class Meta:
      verbose_name_plural = "Ejes"
    def __str__(self):
       return self.nombre 
          

class Ruedas(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    medida = models.CharField(max_length=10)
    dureza = models.CharField(max_length=5)
    color = models.CharField(max_length=10)
    Precio = models.CharField(max_length=20, default='0')
    Cantidad = models.IntegerField( default='0')
    disponible = models.BooleanField(null='false')
    pass  
    class Meta:
      verbose_name_plural = "Ruedas"
    def __str__(self):
       return self.nombre 
          

class Rodamientos(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    dureza = models.CharField(max_length=10)
    Precio = models.CharField(max_length=20, default='0')
    Cantidad = models.IntegerField( default='0')
    disponible = models.BooleanField(null='false')  
    pass
    class Meta:
      verbose_name_plural = "Rodamientos"
    def __str__(self):
       return self.nombre
       
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)

    def __str__(self):
       return self.nombre

class Pedidos(models.Model):
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    numero_pedido = models.CharField(max_length=30, blank=True, null=True)
    tabla = models.ForeignKey(Tabla, on_delete=models.CASCADE, blank=True, null=True)
    rueda = models.ForeignKey(Ruedas, on_delete=models.CASCADE,blank=True, null=True)
    ejes = models.ForeignKey(Ejes, on_delete=models.CASCADE,blank=True, null=True)
    rodamientos = models.ForeignKey(Rodamientos, on_delete=models.CASCADE,blank=True, null=True)
    class Meta:
      verbose_name_plural = "Pedidos"
    def __str__(self):
       return self.numero_pedido


# --- USUARIOS ---

from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

