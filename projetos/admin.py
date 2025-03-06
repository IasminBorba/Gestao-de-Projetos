from django.contrib import admin
from .models import *


class ProjetosForm(admin.ModelAdmin):
    list_display = ['projeto','coordenador','inicio_vigencia', 'fim_vigencia', 'ativo']
    ordering = ['projeto']
    search_fields = ['projeto','coordenador']

admin.site.register(AreasTecnologicas)
admin.site.register(Financiadores)
admin.site.register(Projetos, ProjetosForm)
