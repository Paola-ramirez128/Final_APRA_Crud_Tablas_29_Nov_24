# Generated by Django 5.1 on 2024-11-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto_app', '0004_alter_producto_fecha_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_entrega',
            field=models.DateField(),
        ),
    ]
