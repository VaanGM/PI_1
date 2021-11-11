from django.views.generic.edit import CreateView, FormView
from .models import Municipe, Requisicao
from .forms import MunicipeForm, RequisicaoForm

#Considerar o uso de um Cron Job para reiniciar a numeração das requisições todo ano

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
        form = RequisicaoForm(request.post or None)

    def form_valid(self, form):
        municipe = Municipe() #Cria um objeto de tipo Municipe
        municipe.nome = self.request.session.get('nome') #Copia os valores da sessão para o objeto
        municipe.email = self.request.session.get('email')
        municipe.save() #Salvo o objeto municipe no banco
        #Eu copio os valores e salvo eles no banco aqui e não na outra view para 
        # evitar que um municipe seja inserido no DB sem que junto dele seja criada uma requisição
        requisicao = form.save(commit=False) #salvo o conteudo do form na var requisição
        requisicao.requerente = municipe #salvo o obj municipe no valor do requerente, linkando FK e PK
        try:
            temp = Requisicao.objects.latest('numero')
        except Requisicao.DoesNotExist:
            temp = Requisicao()
            temp.numero=0
        requisicao.numero = temp.numero + 1
        requisicao.save() #Salvo a requisição
        form.save() #salvo o form
        self.request.session['numero_requisicao'] = requisicao.numero
        return super().form_valid(form) # Retorna um httpResponse para a próxima página

class ViewEnviado(CreateView):
    template_name = 'requerimento/enviado.html'
    model = Requisicao
    success_url = '//'
    fields = []
