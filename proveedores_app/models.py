from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    telefono = models.IntegerField()
    gmail = models.CharField(max_length=20)
    raiting = models.FloatField()
    registro_fecha = models.DateField(max_length=30)
    tipo = models.CharField(max_length=20)
    provincia = models.CharField(max_length=30)

    def __str__(self):
        return self.telefono