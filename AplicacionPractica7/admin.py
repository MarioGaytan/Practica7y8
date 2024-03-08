from django.contrib import admin
from .models import CatalogoVideojuegos
# Register your models here.
class CatalogoVideojuegosAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creado",)

admin.site.register(CatalogoVideojuegos,CatalogoVideojuegosAdmin)