from django.db import models

#Models são o layout do banco de dados representado através de conceitos de orientção a objeto
class Municipe(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return "%s" % (self.nome)

class Orgao(models.Model):
    nome = models.CharField(max_length=100)
    gestor = models.CharField(max_length=100)
    #orgao_id = models.IntegerField (primary_key=True)

    def __str__(self):
        return "%s" % (self.nome)

class Requisicao(models.Model):
    
    orgao = models.ForeignKey(Orgao, on_delete = models.CASCADE)
    tema = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    comentario = models.CharField(max_length=500)
    data = models.DateTimeField()
    requerente = models.ForeignKey(Municipe, on_delete = models.CASCADE)

    def __str__(self):
        return "%s" % (self.numero)


