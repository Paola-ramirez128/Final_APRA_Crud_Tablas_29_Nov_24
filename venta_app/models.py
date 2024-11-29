from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    codigo_venta = models.CharField(max_length=9)
    n_cliente = models.IntegerField()
    fecha_venta = models.DateField(max_length=20)
    precio = models.FloatField(max_length=100)
    n_producto = models.IntegerField()
    tipo_pago = models.CharField(max_length=20)

    def __str__(self):
        return self.codigo_venta