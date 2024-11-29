from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.IntegerField(primary_key=True)
    precio=models.FloatField(max_length=10)
    diseno=models.CharField(max_length=10)
    fecha_entrega=models.DateField()
    cantidad=models.PositiveSmallIntegerField()
    tamano=models.CharField(max_length=100)
    def __str__(self):
        return self.precio