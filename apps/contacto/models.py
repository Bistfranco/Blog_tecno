from django.db import models
from django.utils import timezone


# Create your models here.

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=120)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural='Contactos'
        ordering = ['email']

    def __str__(self):
        return self.mensaje
    