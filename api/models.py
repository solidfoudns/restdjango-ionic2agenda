from django.db import models

# Create your models here.
class Orden(models.Model):
    usuario= models.CharField(max_length=50)
    direccion = models.TextField()
    folio = models.PositiveIntegerField()
    fecha_evento = models.DateField()


    def __str__(self):
        return self.usuario