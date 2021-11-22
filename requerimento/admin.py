from django.contrib import admin

from .models import Municipe, Requisicao

admin.site.register(Municipe)


class RequisicaoAdmin(admin.ModelAdmin):
     list_display = ('tema', 'data')

admin.site.register(Requisicao, RequisicaoAdmin)