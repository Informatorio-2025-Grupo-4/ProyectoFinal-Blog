from django.db import models
from genericos.models import Rubro

# Create your models here.

class Producto(models.Model):    #Son clases en Python que se van a relacionar con las tablas.
    
    creado = models.DateTimeField(
        auto_now_add=True
    )
    
    modificado = models.DateTimeField(     #Estos son 2 atributos que van a actualizar la fecha cada vez que se crea y se modifica algo     
        auto_now_add=True
    )
    
    #Djgango me crea por defecto una clave primaria, a menos que nosotros querramos crearla.
    nombre = models.CharField(max_length=30)   #En este tipo de dato es obligatorio poner la longitud máxima
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to = 'productos')     #Esto significa que las imagenes van a estar en una carpeta llamada productos
    rubro = models.ForeignKey(Rubro, null = True, on_delete = models.CASCADE)
    
    #MARCA, RUBRO, SUBRUBRO. Para estos campos vamos a crear tablas. Por ahora lo creamos sin estos campos y después los agregamos. Esto se llama migraciones
    
    def __str__(self):   #Esto es para que cuando yo vea un producto, lo vea a través del nombre
        
        return self.nombre


# MIGRACIONES

# PASOS:
# 1.Verificar que cambios existen
    # python manage.py makemigrations
# 2.Aplicar los cambios
    # python manage.py migrate