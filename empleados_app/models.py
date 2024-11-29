from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=20)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=20)
    sueldo = models.FloatField()
    horario = models.CharField(max_length=20)
    puesto = models.CharField(max_length=20)

    def __str__(self):
        return self.direccion