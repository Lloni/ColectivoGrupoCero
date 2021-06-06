from django.shortcuts import render

# index
def index(request):
    return render(request,"app/index.html")

# artista
def artistas(request):
    return render(request,"app/artistas.html")

# crear_cuenta
def crear_cuenta(request):
    return render(request,"app/crear_cuenta.html")

# detalle_artista
def detalle_artista(request):
    return render(request,"app/detalle_artista.html")

# detalle_obra
def detalle_obra(request):
    return render(request,"app/detalle_obra.html")

# login
def login(request):
    return render(request,"app/login.html")

# obras
def obras(request):
    return render(request,"app/obras.html")

# publicacion
def publicacion(request):
    return render(request,"app/publicacion.html")


