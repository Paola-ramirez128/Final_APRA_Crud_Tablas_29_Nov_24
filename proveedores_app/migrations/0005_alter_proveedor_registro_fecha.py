# Generated by Django 5.1 on 2024-11-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0004_alter_proveedor_raiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='registro_fecha',
            field=models.DateField(max_length=30),
        ),
    ]
