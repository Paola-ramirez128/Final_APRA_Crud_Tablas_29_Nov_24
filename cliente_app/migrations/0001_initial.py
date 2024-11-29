# Generated by Django 5.1.2 on 2024-11-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=30)),
                ('pedidos', models.PositiveSmallIntegerField()),
                ('fecha_resgistro', models.CharField(max_length=30)),
            ],
        ),
    ]
