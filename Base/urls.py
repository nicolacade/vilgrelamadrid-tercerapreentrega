from django.urls import path
from Base import views
from Base.views import formularioClientes, mostrarListado


urlpatterns = [
    path('', views.inicio),
    path('formularioClientes/', views.formularioClientes),
    path('listadoClientes/', views.mostrarListado)
]