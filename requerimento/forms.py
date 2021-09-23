from requerimento.models import Municipe, Requisicao
from django import forms

from django.db import models
 
class MunicipeForm(forms.ModelForm):
    class Meta:
        model = Municipe
        fields = ('nome','email',)
    
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Nome'
        self.fields['email'].label = 'Endereço de E-mail'
        
class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = ('orgao','tema','comentario',)
    
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['orgao'].label = 'Nome'
        self.fields['tema'].label = 'Tema'
        self.fields['comentario'].label = 'Comentários:'