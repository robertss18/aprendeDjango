from django.db import models

# Create your models here.
class miModeloTable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

def __str__(self):
    return f"{self.nombre} {self.apellido}"