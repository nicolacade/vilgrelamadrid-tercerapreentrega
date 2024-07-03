from django.urls import path
from Base import views
from Base.views import formularioClientes, mostrarListado, eliminar_clientes, editar_clientes, ver_cliente


urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('formularioClientes/', views.formularioClientes, name='formulario_clientes'),
    path('listadoClientes/', views.mostrarListado, name= 'mostrar_listado'),
    path('formularioClientes/eliminar/<int:id>/', views.eliminar_clientes, name= 'eliminar_clientes'),
    path('formularioClientes/editar/<int:id>/', views.editar_clientes, name='editar_clientes'),
    path('formularioClientes/<int:id>/', views.ver_cliente, name='ver_clientes'),
    ]