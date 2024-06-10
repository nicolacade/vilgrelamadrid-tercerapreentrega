from django import forms

class ClientesFormulario(forms.Form):
    
    Nombre_cliente = forms.CharField()
    Numero_cliente = forms.IntegerField()
