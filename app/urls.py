from django.urls import path
from .views import index, artistas, contacto, crear_cuenta, detalle_artista,              detalle_obra, login, obras, publicacion

urlpatterns = [
    path('', index, name='index'),
    path('artistas/', artistas, name='artistas'),
    path('contacto/', contacto, name='contacto'),
    path('crear_cuenta/', crear_cuenta, name='crear_cuenta'),
    path('detalle_artista/', detalle_artista, name='detalle_artista'),
    path('detalle_obra/', detalle_obra, name='detalle_obra'),
    path('login/', login, name='login'),
    path('detalle_obra/', detalle_obra, name='detalle_obra'),
    path('obras/', obras, name='obras'),
    path('publicacion/', publicacion, name='publicacion'),
]

