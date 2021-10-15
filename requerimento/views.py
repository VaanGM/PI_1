from django.forms.forms import Form
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404
from django.views.generic.edit import CreateView, FormView

from .models import Municipe, Requisicao
from .forms import MunicipeForm, RequisicaoForm

class ViewIndex(FormView):   
    template_name = 'requerimento/index.html'
    form_class = MunicipeForm
    model = Municipe
    success_url = '/dados/'
 
    def form_new(request): #Cria o Form
        form = MunicipeForm() #Usando os dados de MunicipeForm

    def form_valid(self, form): #Caso os dados inseridos no Form sejam válidos
        print(form.cleaned_data) #---------------------- DEBUG NAS COXA 
        self.request.session['nome'] = form.cleaned_data['nome'] #salva na Sessão o valor do nome inserido no Form
        self.request.session['email'] = form.cleaned_data['email'] #salva na Sessão o valor de email inserido no Form
        return super().form_valid(form)# Retorna um httpResponse para a próxima página
 
class ViewDados(CreateView):
    template_name = 'requerimento/dados.html'
    form_class = RequisicaoForm
    model = Requisicao
    success_url = '/enviado/'

    def form_new(request):
        form = RequisicaoForm(request.post or None) #Devo usar esses parâmetros na função?

    def form_valid(self, form):
        municipe = Municipe() #Cria um objeto de tipo Municipe
        municipe.nome = self.request.session.get('nome') #Copia os valores da sessão para o objeto
        municipe.email = self.request.session.get('email')#Copia os valores da sessão para o objeto
        #Eu faço as cópias dos valores aqui e não na outra tela para evitar que um municipe seja inserido no DB
        #sem que junto dele seja criada uma requisição
        municipe.save() #Salvo o objeto municipe no banco
        #municipe.pk faz referencia a chave primaria do municipe...
        #COMO É QUE EU SALVO ESSA DESGRAÇA de PK NA FK DA REQUISIÇÃO
        #TAQUEPARIU
        #Cannot assign "Valor da PK de municipe": "Requisicao.requerente" must be a "Municipe" instance.
        #COMO ASSIM, CARALHO?
        #TESTANDO ALTOS ROLE AQUI --------------
        requisicao = form.save(commit=False) #salvo o conteudo do form na var requisição
        requisicao.requerente = municipe #salvo o obj municipe no valor do requerente, linkando FK e PK
        requisicao.save() #Salvo a requisição, não sei ao certo qual magia rola aqui
        form.save() #salvo o form
        return super().form_valid(form) # Retorna um httpResponse para a próxima página
        #NÃO ACREDITO QUE ESSA BAGUNÇA FUNCIONA, UFA
        #TEMOS INSERÇÃO FUNCIONAL DE DADOS NO BANCO!!!!!!!!!! SEXTOU!!!!!!!!

class ViewEnviado(generic.DetailView):
    template_name = 'requerimento/enviado.html'
    model = Requisicao
    slug_field = 'tema'
    
    def detail_new(request):
        try:
            queryset = Requisicao.objects.get(request.session.get('id'))
        except:
            raise Http404
        req = get_object_or_404(Requisicao, pk=id)
        return render(request, 'requerimento/requerimento.html')
        #p = get_object_or_404(Poll, pk=poll_id)