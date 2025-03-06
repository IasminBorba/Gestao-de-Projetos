from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Colaboradores
from .serializers import ColaboradoresSerializer


class ColaboradoresView(viewsets.ModelViewSet):
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradoresSerializer

    @action(detail=False, methods=['get'])
    def listar(self, request):
        colaboradores = Colaboradores.objects.all().order_by('nome')
        return Response(ColaboradoresSerializer(colaboradores, many=True).data)


    @action(detail=False, methods=['post'])
    def cadastrar(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

        return Response({'message': 'Colaborador cadastrado com sucesso!'})


    @action(detail=False, methods=['get'], url_path='(?P<id_colaborador>[^/.]+)/visualizar')
    def visualizar(self, request, id_colaborador=None):
        try:
            colaborador = Colaboradores.objects.get(id_colaborador=id_colaborador)
            return Response(colaborador.data)
        except:
            return Response({'message': 'Colaborador não encontrado'})


    @action(detail=False, methods=['patch'], url_path='(?P<id_colaborador>[^/.]+)/editar')
    def editar(self, request, id_colaborador=None):
        try:
            colaborador = Colaboradores.objects.get(id_colaborador=id_colaborador)
        except:
            return Response({'message': 'Colaborador não encontrado'})

        serializer = self.serializer_class(colaborador, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Colaborador atualizado com sucesso'})
        else:
            return Response(serializer.errors)
