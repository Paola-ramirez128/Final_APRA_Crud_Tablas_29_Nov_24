# Generated by Django 5.1.2 on 2024-11-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='id_proveedor',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='registro_fecha',
            field=models.DateField(max_length=30),
        ),
    ]
