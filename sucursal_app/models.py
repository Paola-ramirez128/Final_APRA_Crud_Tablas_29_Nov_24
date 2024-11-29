from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=30)
    nombre = models.CharField(max_length=20)
    encargado = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.direccion