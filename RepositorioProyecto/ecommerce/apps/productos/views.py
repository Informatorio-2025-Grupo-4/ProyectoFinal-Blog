from django.shortcuts import render
from django.views.generic.detail import DetailView    #Esto es una vista preparada para mostrar el detalle de un proyecto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Producto, Rubro            #Esto es necesario para traer lo que está en la clase Producto
from .forms import FormularioCrearProducto, FormularioModificarProducto


# Los únicos 2 tipos de vistas que tenemos son basadas en funciones o clases


#VISTA BASADA EN FUNCIONES
def Listar_Productos(request):
    
    
    #Para listar los productos uso la ORM
    
    #ORM = SELECT * FROM PRODUCTO
    todos = Producto.objects.all()    #Acá le digo que me traiga todos los objetos de la tabla productos
    
    #ORM CON FILTRO
    #ORM = SELECT * FROM PRODUCTO WHERE STOCK MAYOR que 0
    solo_stock = Producto.objects.filter(stock__gt = 0)    #Esto quiere decir que sea mayor que 0. stock es el nombre del atributo y gt significa mayor
    #__gte significa mayor o igual
    #__lt significa menor
    #__lte significa menor o igual
    
    #Para mostrar por ejemplo los productos con stock mayor que 0 y otro filtro, necesitaríamos agregar lógica. Poner un botón.
    
    
    return render(request, 'productos/listar.html', {'productos':solo_stock})       #Esto es para pasarle todos los productos al template. Es una lista


#Vista basada en funcion
def Detalle_Producto(request, pk):
    
    p = Producto.objects.get(pk = pk)   #Esto solamente me va a traer 1 producto que cumple esa condición. A diferencia de filter que puede tratar varios.
    
    return render(request, 'Productos/Detalle.html',{'producto':p})         #p es un solo objeto



#VISTA BASADA EN CLASES
class Detalle_Producto_Clase(DetailView):
    
    template_name = 'Productos/Detalle.html'
    model = Producto
    context_object_name = 'producto'   #Si yo no le paso esto, en el template de detalle, voy a tener que cambiar la palabra producto por una genérica, que es object

#La diferencia está en que la url se escribe distinta. Lo anterior es una funcion que hace lo que yo le digo y nada más. 
#Pero esto es una clase y tiene el poder de heredar cosas.

#Algo muy importante es que, a diferencia de la función anterior, no hace falta poner la condición del pk.


class Crear_Producto(CreateView):     
    
    model = Producto
    template_name = 'productos/crear.html'
    form_class = FormularioCrearProducto
    success_url = reverse_lazy('productos:path_listar_productos')
    
    
class Modificar_Producto(UpdateView):     
    
    model = Producto
    template_name = 'productos/modificar.html'
    form_class = FormularioModificarProducto
    success_url = reverse_lazy('productos:path_listar_productos')
    

class Borrar_Producto(DeleteView):     
    
    model = Producto                    #A diferencia de los 2 anteriores, no necesito ni un forms pq no hay que llenar nada, ni un template pq tampoco debo mostrar nada
    success_url = reverse_lazy('productos:path_listar_productos')    
    
    
    
def Filtrar_Rubro(request, pk):
    
    rubro_filtrado = Rubro.objects.get(pk = pk)
    
    productos_filtrados = Producto.objects.filter(rubro = rubro_filtrado)
    
    return render(request, 'productos/filtrados.html', {'productos': productos_filtrados,'nombre_rubro': rubro_filtrado.nombre})


