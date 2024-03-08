from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CatalogoVideojuegos(models.Model):
    nombre=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    publicoObjaetivo=models.CharField(max_length=50)
    plataforma=models.CharField(max_length=50, choices=[("Xbox","Xbox"),("Playstation","Playstation"),("Computadora","Computadora")])
    fecha_creado=models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre}-{self.genero}-{self.fecha_creado}"