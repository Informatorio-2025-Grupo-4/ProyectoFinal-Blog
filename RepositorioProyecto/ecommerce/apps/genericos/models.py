from django.db import models

# Create your models here.

class Rubro(models.Model):
    
    nombre = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to= 'rubros', null= True)
    
    def __str__(self):
        return self.nombre