from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from datetime import datetime
from django.views.generic.edit import CreateView, FormView

from .models import Municipe, Orgao, Requisicao
from .forms import MunicipeForm, RequisicaoForm


#Pra chamar uma view, é preciso mapea-la para uma URL, no arquivo urls.py, neste mesmo app.
#Pesquisar sobre *args e **kwargs ------

class ViewIndex(FormView):
    
    template_name = 'requerimento/index.html'
    form_class = MunicipeForm
    success_url = '/dados/'


    def form_new(request):
        form = MunicipeForm()
        return render('requerimento/index.html', {'form': form})

    def form_valid(self, form):
        return super().form_valid(form)

class ViewDados(CreateView):
    template_name = 'requerimento/dados.html'
    form_class = RequisicaoForm
    model = Requisicao
    success_url = '/enviado/'

    def form_new(request):
        form = MunicipeForm()
        return render('requerimento/index.html', {'form': form})

    def form_valid(self, form):
        form.data = datetime.now()
        return super().form_valid(form)

class ViewEnviado(generic.DetailView):
    #model = Requisicao
    template_name = 'requerimento/enviado.html'

    #def form_new(request):
    #    form = MunicipeForm()
    #    return render('requerimento/enviado.html', {'form': form})

    #def form_valid(self, form):
    #    return super().form_valid(form)


#def registros(request):
#    ultimas_requisicoes = Requisicao.objects.order_by('-data')[:5]
#    output = ', '.join([q.question_text for q in ultimas_requisicoes])
#    context = {'ultimas_requisicoes': ultimas_requisicoes}
#   return render(request, 'requerimento/registros.html', context)