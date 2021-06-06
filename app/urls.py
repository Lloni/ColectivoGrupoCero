from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.artistas, name='artistas'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('detalle_artista/', views.detalle_artista, name='detalle_artista'),
    path('detalle_obra/', views.detalle_obra, name='detalle_obra'),
    path('login/', views.login, name='login'),
    path('detalle_obra/', views.detalle_obra, name='detalle_obra'),
    path('obras/', views.obras, name='obras'),
    path('publicacion/', views.publicacion, name='publicacion'),
]
