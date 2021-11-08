from requerimento.models import Municipe, Requisicao
from django import forms
 
class MunicipeForm(forms.ModelForm):
    class Meta:
        model = Municipe
        fields = ('nome','email',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input_field'}),
            'email': forms.TextInput(attrs={'class': 'input_field'})
        }

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Nome'
        self.fields['email'].label = 'Endereço de E-mail'
        
class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = Requisicao
        fields = ('tema','comentario',)
        widgets = {
            'tema': forms.TextInput(attrs={'class': 'input_field', 'placeholder': 'Ex: Troca de lâmpada, Tapa-buraco, etc.'}),
            'comentario': forms.Textarea(attrs={'class': 'input_field', 
                'placeholder': 'Informações relevantes para a identificação e execução do serviço requisitado.'})
        }
    
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['tema'].label = 'Assunto:'
        self.fields['comentario'].label = 'Comentários:'