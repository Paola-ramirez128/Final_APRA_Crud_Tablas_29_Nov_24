from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=20)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=20)
    correo=models.CharField(max_length=30)
    pedidos=models.PositiveSmallIntegerField()
    fecha_registro=models.DateField()

    def __str__(self):
        return self.nombre