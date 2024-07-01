from django.db import models

class Cliente(models.Model):

    nombre_cliente = models.CharField(max_length=60)
    apellido_cliente = models.CharField(max_length=60)
    telefono_cliente = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"
