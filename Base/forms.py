from django import forms


class ClientesFormulario(forms.Form):
    
    Numero_cliente = forms.IntegerField()
    Nombre_cliente = forms.CharField()
