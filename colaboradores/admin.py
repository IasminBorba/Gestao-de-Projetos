from django.contrib import admin
from .models import Colaboradores


class ColaboradoresForm(admin.ModelAdmin):
    list_display = ['nome','cpf','dt_nascimento']
    ordering = ['nome']
    search_fields = ['nome','cpf']

admin.site.register(Colaboradores, ColaboradoresForm)
