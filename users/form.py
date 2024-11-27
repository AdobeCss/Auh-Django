from django.contrib.auth import forms
from django import forms

class Form_add_user(forms.Form):

    name = forms.CharField(label="Digite seu nome", max_length=100)
    email = forms.EmailField(label="Digite seu Email", max_length=100)
    password = forms.CharField(max_length=6,label='Digite sua senha')

    def __init__(self, *args, **kwargs): # Adiciona 
                super().__init__(*args, **kwargs)  
                for field_name, field in self.fields.items():   
                    field.widget.attrs['class'] = 'form-control'