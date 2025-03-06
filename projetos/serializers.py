from rest_framework import serializers
from .models import *
from colaboradores.serializers import ColaboradoresSerializer

class AreasTecnologicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasTecnologicas
        fields = '__all__'

class FinanciadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiadores
        fields = '__all__'

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'

    def to_representation(self, obj):
        try:
            equipe = ColaboradoresSerializer(obj.equipe.all(), many=True).data
        except Exception as e:
            equipe = None
            
        financiador = {
            'id_financiador': obj.id_financiador.pk,
            'financiador': obj.id_financiador.financiador
        }
        area_tecnologica = {
            'id_area_tecnologica': obj.id_area_tecnologica.pk,
            'area_tecnologica': obj.id_area_tecnologica.area_tecnologica
        }

        res = {
            'id_projeto': obj.id_equipe_projeto,
            'projeto': obj.projeto,
            'financiador': financiador,
            'area_tecnologica': area_tecnologica,
            'coordenador': obj.coordenador,
            'ativo': obj.ativo,
            'inicio_vigencia': obj.inicio_vigencia,
            'fim_vigencia': obj.fim_vigencia,
            'valor': obj.valor,
            'qtd_membros': obj.qtd_membros,
            'equipe': equipe,
        }

        return res
        