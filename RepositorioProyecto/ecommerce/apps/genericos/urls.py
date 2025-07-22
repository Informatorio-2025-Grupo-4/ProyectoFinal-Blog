

from django.urls import path 

from . import views

app_name = "genericos"      #Esto me indica como se llama la aplicación

urlpatterns = [
    
    path('Rubros', views.Listar_Rubros, name = "path_listar_rubros"),


]