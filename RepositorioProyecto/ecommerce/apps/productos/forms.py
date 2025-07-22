
from django import forms 

from .models import Producto


class FormularioCrearProducto(forms.ModelForm):    #Esta clase hereda de una clase que está preparada para crear un formulario a partir de un modelo
    
    class Meta: 
        model = Producto                #Este sería el modelo. Se lo pasamos
        fields = ('nombre','stock','precio','imagen','rubro')         #Acá le decimos qué campos queremos que aparezcan
        
        
class FormularioModificarProducto(forms.ModelForm):    #Esta clase hereda de una clase que está preparada para crear un formulario a partir de un modelo
    
    class Meta: 
        model = Producto                #Este sería el modelo. Se lo pasamos
        fields = ('stock','precio','imagen')         #Acá le decimos qué campos queremos que aparezcan