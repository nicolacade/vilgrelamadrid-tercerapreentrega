from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Aerosoles, Textiles
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def productos(request):
    return render(request, 'productos/inicio_productos.html')
    
class Aerosol(LoginRequiredMixin, ListView):
    model = Aerosoles
    template_name = 'productos/aerosoles.html'
    context_object_name = 'aerosoles'

class AgregarFraganciaAerosol(CreateView):
     model = Aerosoles
     template_name = 'productos/crear_fragancia_aerosol.html'
     success_url = reverse_lazy('aerosoles')
     fields = ['fragancia', 'stock', 'fecha_vencimiento']

class VerAerosol(DetailView):
    model = Aerosoles
    template_name = 'productos/ver_aerosol.html'

class EditarFraganciaAerosol(UpdateView):
    model = Aerosoles
    template_name = 'productos/editar_aerosol.html'
    success_url = reverse_lazy('aerosoles')
    fields = ['fragancia', 'stock', 'fecha_vencimiento']
    
class EliminarFraganciaAerosol(DeleteView):
    model = Aerosoles
    template_name = "productos/eliminar_aerosol.html"
    success_url = reverse_lazy('aerosoles')
#------------------------------------------------------
    
class Textil(LoginRequiredMixin, ListView):
    model = Textiles
    template_name = 'productos/textiles.html'
    context_object_name = 'textiles'

class AgregarFraganciaTextil(CreateView):
     model = Textiles
     template_name = 'productos/crear_fragancia_textil.html'
     success_url = reverse_lazy('textiles')
     fields = ['fragancia', 'stock', 'fecha_vencimiento']

class VerTextil(DetailView):
    model = Textiles
    template_name = 'productos/ver_textil.html'

class EditarFraganciaTextil(UpdateView):
    model = Textiles
    template_name = 'productos/editar_textil.html'
    success_url = reverse_lazy('textiles')
    fields = ['fragancia', 'stock', 'fecha_vencimiento']
    
class EliminarFraganciaTextil(DeleteView):
    model = Textiles
    template_name = "productos/eliminar_textil.html"
    success_url = reverse_lazy('textiles')