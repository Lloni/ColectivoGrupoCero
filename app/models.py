from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=30,verbose_name='Nombre')
    correo = models.CharField(max_length=40,verbose_name='Correo')
    password = models.CharField(max_length=20,verbose_name='Password')

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre_artista = models.CharField(max_length=50, verbose_name='Nombre')
    pais_artista = models.CharField(max_length=50, verbose_name='Pais')
    descripcion = models.TextField(max_length=500, verbose_name='Historia')
    foto = models.ImageField(verbose_name='Imagen', upload_to='proyects')

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"

    def __str__(self):
        return self.nombre_artista

class Obra(models.Model):
    nombre_obra = models.CharField(max_length=40,verbose_name='Nombre de la obra')
    anio = models.CharField(max_length=4,verbose_name='Año')
    precio = models.CharField(max_length=9, verbose_name='Precio ($CLP)')
    tipo_obra = models.CharField(max_length=20,verbose_name='Tipo de obra')
    alto = models.CharField(max_length=4,verbose_name='Alto')
    ancho = models.CharField(max_length=4,verbose_name='Ancho')
    largo = models.CharField(max_length=4,verbose_name='largo')
    soporte = models.CharField(max_length=20,verbose_name='Soporte')
    descripcion = models.TextField(max_length=250,verbose_name='Descripción')
    imagen = models.ImageField(verbose_name='Imagen', upload_to = 'proyects')

    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
    
    def __str__(self):
        return self.nombre_obra