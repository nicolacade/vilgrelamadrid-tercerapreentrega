from django.shortcuts import render
from .models import Clientes
from django.http import HttpResponse
from .forms import ClientesFormulario

def inicio (request):
    return render (request, 'inicio/template1.html')

def formularioClientes(request):

      if request.method == 'POST':

            formulario = ClientesFormulario(request.POST)

            print(formulario)

            if formulario.is_valid: 

                  informacion = formulario.cleaned_data

                  clientes = Clientes(nombre_corto_cliente=informacion['Nombre_cliente'], numero_cliente=informacion['Numero_cliente']) 

                  clientes.save()

                  return render(request, "inicio/template1.html") 

      else: 

            formulario= ClientesFormulario()

      return render(request, "inicio/formularioClientes.html", {"formulario":formulario})

def mostrarListado(request):
      clientes = Clientes.objects.all()
      return render (request, 'inicio/mostrar_listado.html', {'clientes' : clientes})