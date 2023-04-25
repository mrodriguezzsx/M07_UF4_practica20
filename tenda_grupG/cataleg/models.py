from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50) 
    descripcion = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)


