from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClientesFormulario, BuscarCliente, EditarCliente
from django.contrib.auth.decorators import login_required
def inicio (request):
    return render (request, 'inicio/inicio_mensaje.html')

def formularioClientes(request):
      if request.method == 'POST':
            formulario = ClientesFormulario(request.POST, request.FILES)
            print(formulario)
            if formulario.is_valid(): 
                  informacion = formulario.cleaned_data
                  clientes = Cliente(nombre_cliente=informacion['nombre_cliente'], apellido_cliente =informacion['apellido_cliente'], telefono_cliente=informacion['telefono_cliente'], fecha_nacimiento = informacion ['fecha_nacimiento'], foto_perfil=informacion['foto_perfil'])
                  clientes.save()
                  return redirect("mostrar_listado") 
      else: 
            formulario= ClientesFormulario()
      return render(request, "inicio/formularioClientes.html", {"formulario":formulario})

def mostrarListado(request):
      formulario_clientes = BuscarCliente(request.GET)
      if formulario_clientes.is_valid():
            nombre = formulario_clientes.cleaned_data['nombre_cliente']
            nombres = Cliente.objects.filter(nombre_cliente__icontains=nombre)
      else:
            nombres = Cliente.objects.all()
      return render (request, 'inicio/mostrar_listado.html', {'clientes' : nombres , 'formulario_clientes' : formulario_clientes})

@login_required
def eliminar_clientes (request,id):
      nombre = Cliente.objects.get(id=id)
      nombre.delete()
      return redirect('mostrar_listado')

@login_required
def editar_clientes(request,id):
      nombre = Cliente.objects.get(id=id)
      formulario = EditarCliente(initial={'nombre_cliente': nombre.nombre_cliente , 'apellido_cliente' : nombre.apellido_cliente, 'telefono_cliente': nombre.telefono_cliente})
      if request.method == 'POST':
            formulario = EditarCliente(request.POST)
            if formulario.is_valid():
                  info = formulario.cleaned_data 
                  nombre.nombre_cliente = info ['nombre_cliente']
                  nombre.apellido_cliente = info ['apellido_cliente']
                  nombre.telefono_cliente = info ['telefono_cliente']
                  nombre.save()
                  return redirect('mostrar_listado')
            
      return render(request, 'inicio/editar_clientes.html' , {'formulario': formulario , 'nombre': nombre})

def ver_cliente(request,id):
      nombre = Cliente.objects.get(id=id)
      return render (request, 'inicio/ver_cliente.html', {'nombre': nombre})