from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView

from .models import Municipe, Orgao, Requisicao
from .forms import MunicipeForm


#Pra chamar uma view, é preciso mapea-la para uma URL, no arquivo urls.py, neste mesmo app.

class ViewIndex(FormView):
    
    template_name = 'requerimento/index.html'
    form_class = MunicipeForm
    objeto_contexto = 'dados_requerimento'
    success_url = '/enviado/'


    def form_new(request):
        form = MunicipeForm()
        return render('requerimento/index.html', {'form': form})

    def form_valid(self, form):
        return super().form_valid(form)


class ViewEnviado(generic.DetailView):
    model = Requisicao
    template_name = 'requerimento/index.html'


#def registros(request):
#    ultimas_requisicoes = Requisicao.objects.order_by('-data')[:5]
#    output = ', '.join([q.question_text for q in ultimas_requisicoes])
#    context = {'ultimas_requisicoes': ultimas_requisicoes}
#   return render(request, 'requerimento/registros.html', context)