# Generated by Django 5.0.3 on 2024-03-08 05:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoVideojuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('publicoObjaetivo', models.CharField(max_length=50)),
                ('plataforma', models.CharField(choices=[('Xbox', 'Xbox'), ('Playstation', 'Playstation'), ('Computadora', 'Computadora')], max_length=50)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]