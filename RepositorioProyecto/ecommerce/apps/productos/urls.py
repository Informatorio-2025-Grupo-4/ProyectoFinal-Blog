
from django.urls import path

from . import views

app_name = "productos"      #Esto me indica como se llama la aplicación

urlpatterns = [
    
    path('Listar', views.Listar_Productos, name = "path_listar_productos"),
    #path('Detalle/<int:pk>', views.Detalle_Producto, name = "path_detalle_producto"),
    path('Detalle/<int:pk>', views.Detalle_Producto_Clase.as_view(), name = "path_detalle_producto"),   #Esta vista y la anterior hacen lo mismo. Solo puedo usar una
    
    path('Crear/', views.Crear_Producto.as_view(), name = 'path_crear_producto'),   #Esto es una opcion para cargar productos
    path('Modificar/<int:pk>', views.Modificar_Producto.as_view(), name = 'path_modificar_producto'),    #Esto es una opcion para modificar prod. Acá uso el pk porque sí me fijo en un único producto ya creado
                                                                        #El as_view() se usa porque es una clase
    path('Eliminar/<int:pk>', views.Borrar_Producto.as_view(), name = 'path_borrar_producto'),
    
    
    #Filtro por rubro
    path('Filtrados/<int:pk>', views.Filtrar_Rubro , name= 'path_filtro_rubro')
    

]