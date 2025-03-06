from django.db import models
from colaboradores.models import Colaboradores


class AreasTecnologicas(models.Model):
    id_area_tecnologica = models.AutoField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100)

    class Meta:
        db_table = 'projetos"."AreasTecnologicas'
        verbose_name_plural = 'Áreas Tecnológicas'

    def __str__(self):
        return self.area_tecnologica


class Financiadores(models.Model):
    id_financiador = models.AutoField(primary_key=True)
    financiador = models.CharField(max_length=100)

    class Meta:
        db_table = 'projetos"."Financiadores'
        verbose_name_plural = 'Financiadores'

    def __str__(self):
        return self.financiador


class Projetos(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100)
    id_financiador = models.ForeignKey(Financiadores, on_delete=models.CASCADE)
    id_area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.CASCADE)
    coordenador = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()
    valor = models.FloatField()
    qtd_membros = models.IntegerField(default=0)
    equipe = models.ManyToManyField(Colaboradores, blank=True, symmetrical=False, related_name='equipe', db_table='projeto"."EquipeProjeto',)

    class Meta:
        db_table = 'projetos"."Projetos'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.projeto

    def atualizar_qtd_membros(self):
        self.qtd_membros = self.equipe.count()
        self.save()