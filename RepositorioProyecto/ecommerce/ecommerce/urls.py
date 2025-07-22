

from django.contrib import admin
from django.urls import path, include

from . import views

from django.conf.urls.static import static     #Estas 2 importaciones son para poder ver las imágenes
from django.conf import settings

urlpatterns = [                      #Django va a fijarse cual es la url, y la que coincida con la de acá, nos va a devolver esa vista. En nuestro caso todavía es vacía
    path('admin/', admin.site.urls),    #Esto es algo que django trae por defecto. Si ponemos localhost.8000/admin, nos va a llevar a un apartado de autenticación
    
    #1er parametro: la url. (Es una url vacía)
    #2do parametro: la vista que se ejecuta
    #3er parametro: el nombre de este path
    path('', views.Home, name = "path_home"),
    
    
    #En el from de arriba agregamos include
    #Eso es para enlazar la url de productos a esta rama general de urls
    #Si no hacemos esto, django no lo va a encontrar, porque siempre django se fija en esta rama de urls
    path('Productos/', include('productos.urls')),
    #Esto quiere decir que si la url comienza con: Productos, el encargado de productos es el archivo urls que está en la carpeta productos.
    
    
    path('Genericos/', include('genericos.urls')),
    
    
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       #Esto es para poder ver las imágenes
