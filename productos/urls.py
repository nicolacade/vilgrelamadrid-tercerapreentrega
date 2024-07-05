from django.urls import path
from . import views  

urlpatterns = [
    path('',views.productos ,name='productos'),
    path('aerosoles/', views.Aerosol.as_view() , name='aerosoles'),
    path('aerosoles/crear/', views.AgregarFraganciaAerosol.as_view() , name='crear_fragancia_aerosol'),
    path('aerosoles/<int:pk>/', views.VerAerosol.as_view() , name='ver_aerosol'),
    path('aerosoles/<int:pk>/editar/', views.EditarFraganciaAerosol.as_view() , name='editar_aerosol'),
    path('aerosoles/<int:pk>/eliminar/', views.EliminarFraganciaAerosol.as_view() , name='eliminar_aerosol'),
    path('textiles/', views.Textil.as_view() , name='textiles'),
    path('textiles/crear/', views.AgregarFraganciaTextil.as_view() , name='crear_fragancia_textil'),
    path('textiles/<int:pk>/', views.VerTextil.as_view() , name='ver_textil'),
    path('textiles/<int:pk>/editar/', views.EditarFraganciaTextil.as_view() , name='editar_textil'),
    path('textiles/<int:pk>/eliminar/', views.EliminarFraganciaTextil.as_view() , name='eliminar_textil')
]
