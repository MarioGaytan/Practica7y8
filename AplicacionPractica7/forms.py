from django.forms import ModelForm
from .models import CatalogoVideojuegos

class CatalogoForm(ModelForm):
    class Meta:
        model=CatalogoVideojuegos
        fields=[
            'nombre',
            'genero',
            'publicoObjaetivo',
            'plataforma'
        ]