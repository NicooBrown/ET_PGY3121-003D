# Generated by Django 4.2.2 on 2023-06-25 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('numero_telefono', models.CharField(max_length=9)),
                ('comentario', models.TextField()),
            ],
        ),
    ]
