from django.db import models

class Clientes(models.Model):

    nombre_corto_cliente = models.CharField(max_length=30)
    numero_cliente = models.IntegerField()

class InfoClientes(models.Model):
    nombre =  models.CharField(max_length=30)
    apellido =  models.CharField(max_length=30)
    telefono =  models.IntegerField()