from django.contrib import admin
from .models import *


class EquipeProjetoInline(admin.TabularInline):
    model = Projetos.equipe.through
    extra = 1
    verbose_name = 'Colaborador'
    verbose_name_plural = 'Equipe'

class ProjetosForm(admin.ModelAdmin):
    list_display = ['projeto','coordenador','inicio_vigencia', 'fim_vigencia', 'ativo']
    ordering = ['projeto']
    search_fields = ['projeto','coordenador']
    exclude = ('equipe',)
    inlines = [EquipeProjetoInline]

admin.site.register(AreasTecnologicas)
admin.site.register(Financiadores)
admin.site.register(Projetos, ProjetosForm)
