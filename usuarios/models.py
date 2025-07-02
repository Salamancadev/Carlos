from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    documento = models.CharField(max_length=20, unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre_completo