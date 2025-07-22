from django.shortcuts import render

def Home(request):       # Esto es una vista que no tiene lógica incorporada. Nos va a servir para levantar un template

    return render(request, 'home.html')

