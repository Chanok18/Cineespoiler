from django.db import models

class Genero(models.Model):  
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.IntegerField()

    
    generos = models.ManyToManyField(Genero)  

    def __str__(self):
        return self.titulo