from django.contrib.auth import forms
from django import forms

class Form_add(forms.Form):
    name = forms.CharField(label="Digite nome do perfil", max_length=100)
    def __init__(self, *args, **kwargs): # Adiciona 
                super().__init__(*args, **kwargs)  
                for field_name, field in self.fields.items():   
                    field.widget.attrs['class'] = 'form-control'
                    
                    
class Form_update(forms.Form):
    name = forms.CharField(label="Digite o novo nome do perfil", max_length=100)
    def __init__(self, *args, **kwargs): # Adiciona 
                super().__init__(*args, **kwargs)  
                for field_name, field in self.fields.items():   
                    field.widget.attrs['class'] = 'form-control'