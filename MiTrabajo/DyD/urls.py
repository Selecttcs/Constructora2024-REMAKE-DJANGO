from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
    path('Recursos', views.recursos, name='Recursos'),
    path('Inventario', views.inventario, name='Inventario'),
]
