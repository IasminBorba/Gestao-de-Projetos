from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *
from colaboradores.models import Colaboradores
from colaboradores.serializers import ColaboradoresSerializer


class AreasTecnologicasView(viewsets.ModelViewSet):
    queryset = AreasTecnologicas.objects.all()
    serializer_class = AreasTecnologicasSerializer

    @action(detail=False, methods=['get'])
    def listar(self, request):
        areasTecnologicas = AreasTecnologicas.objects.all().order_by('area_tecnologica')
        return Response(AreasTecnologicasSerializer(areasTecnologicas, many=True).data)


class FinanciadoresView(viewsets.ModelViewSet):
    queryset = Financiadores.objects.all()
    serializer_class = FinanciadoresSerializer

    @action(detail=False, methods=['get'])
    def listar(self, request):
        financiadores = Financiadores.objects.all().order_by('financiador')
        return Response(FinanciadoresSerializer(financiadores, many=True).data)


class ProjetosView(viewsets.ModelViewSet):
    queryset = Projetos.objects.all()
    serializer_class = ProjetosSerializer

    @action(detail=False, methods=['get'])
    def form(self, request):
        dados = []
        dados['financiadores'] = FinanciadoresSerializer(Financiadores.objects.all().order_by('financiador'), many=True).data
        dados['areas_tecnologicas'] = AreasTecnologicasSerializer(AreasTecnologicas.objects.all().order_by('area_tecnologica'), many=True).data
        dados['equipe'] = ColaboradoresSerializer(Colaboradores.objects.all().order_by('nome'), many=True).data

        return Response(dados)

    @action(detail=False, methods=['get'])
    def listar(self, request):
        projetos = Projetos.objects.all().order_by('projeto')
        return Response(ProjetosSerializer(projetos, many=True).data)

    @action(detail=False, methods=['post'])
    def cadastrar(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        return Response({'message': 'Projeto cadastrado com sucesso!'})

    @action(detail=False, methods=['post'], url_path='(?P<id_projeto>[^/.]+)/inativar')
    def inativar(self, request, id_projeto=None):
        try:
            projeto = Projetos.objects.get(id_projeto=id_projeto)
            projeto.ativo = False
            projeto.save()
            
            return Response({'message': 'Projeto inativo'})
        except:
            return Response({'message': 'Projeto não encontrado'})

    @action(detail=False, methods=['patch'], url_path='(?P<id_projeto>[^/.]+)/editar')
    def editar(self, request, id_projeto=None):
        try:
            projeto = Projetos.objects.get(id_projeto=id_projeto)
        except:
            return Response({'message': 'Projeto não encontrado'})

        serializer = self.serializer_class(projeto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Projeto atualizado com sucesso'})
        else:
            return Response(serializer.errors)

    @action(detail=False, methods=['get'], url_path='(?P<id_projeto>[^/.]+)/visualizar')
    def visualizar(self, request, id_projeto=None):
        try:
            projeto = Projetos.objects.get(id_projeto=id_projeto)
            return Response(projeto.data)
        except:
            return Response({'message': 'Projeto não encontrado'})

    @action(detail=False, methods=['get'], url_path='(?P<id_projeto>[^/.]+)/equipe')
    def visualizar_equipe(self, request, id_projeto=None):
        try:
            projeto = Projetos.objects.get(id_projeto=id_projeto)
        except:
            return Response({'message': 'Projeto não encontrado'})

        return Response(ColaboradoresSerializer(projeto.equipe.all(), many=True).data)

    @action(detail=False, methods=['patch'], url_path='(?P<id_projeto>[^/.]+)/equipe/atualizar')
    def atualizar_equipe(self, request, id_projeto=None):
        try:
            projeto = Projetos.objects.get(id_projeto=id_projeto)
        except:
            return Response({'message': 'Projeto não encontrado'})

        for colaborador_data in request.data['equipe']:
            try:
                colaborador = Colaboradores.objects.get(id_colaborador=colaborador_data['id_colaborador'])
                serializer = ColaboradoresSerializer(colaborador, data=colaborador_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors)
            except Colaboradores.DoesNotExist:
                return Response({'message': 'Colaborador não encontrado'})

        return Response({'message': 'Equipe atualizada com sucesso'})