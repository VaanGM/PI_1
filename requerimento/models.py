from django.db import models
from django.urls import reverse
from datetime import datetime 
from django.utils import timezone

class Municipe(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return "%s" % (self.nome)
      
    def get_absolute_url(self):
        return reverse('municipe-detail', kwargs={'pk': self.pk})

class Requisicao(models.Model):

    tema = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    comentario = models.CharField(max_length=3000)
    data = models.DateTimeField(default=timezone.now, blank=True)
    requerente = models.ForeignKey(Municipe, on_delete = models.CASCADE)

    def __str__(self):
        return "%s" % (self.numero)
    
    def get_absolute_url(self):
        return reverse('requisicao-detail', kwargs={'pk': self.pk})