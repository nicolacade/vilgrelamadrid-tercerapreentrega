from django.db import models

class Aerosoles(models.Model):
    fragancia = models.CharField(max_length=20)
    stock = models.IntegerField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f'{self.fragancia}'

class Textiles(models.Model):
    fragancia = models.CharField(max_length=20)
    stock = models.IntegerField()
    fecha_vencimiento = models.DateField()
    
    def __str__(self):
        return f'{self.fragancia}'