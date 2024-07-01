from django import forms

class ClientesFormulario(forms.Form):
    
    nombre_cliente = forms.CharField(max_length=60)
    apellido_cliente = forms.CharField(max_length=60)
    telefono_cliente = forms.IntegerField()
   
class BuscarCliente(forms.Form):
    nombre_cliente = forms.CharField(max_length=20, required=False)

class EditarCliente(ClientesFormulario):
    ...
    