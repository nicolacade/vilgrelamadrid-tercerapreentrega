from django.urls import path
from Base import views
from Base.views import agregar_clientes


urlpatterns = [
    path('', views.inicio),
    path('AgregoCliente/', views.agregar_clientes),
    path('formularioClientes', views.formularioClientes)
]