from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Usado na api version 2
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
API version 1
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request, *args, **kwargs):  # Sobrescrevendo o método create
        response = super().create(request, *args, **kwargs)
        return Response({"mensagem": "Curso criado com sucesso!", "dados": response.data}, status=status.HTTP_201_CREATED)


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get("curso_pk"):
            # Filtra as avaliações pelo curso informado na URL (curso_pk) e retorna todas as avaliações deste curso (curso_id).
            return self.queryset.filter(curso_id=self.kwargs.get("curso_pk"))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get("curso_pk"):
            # Filtra as avaliações pelo curso informado na URL (curso_pk) e retorna a avaliação do curso informado (curso_id) com o id informado (avaliacao_pk).
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get("curso_pk"), pk=self.kwargs.get("avaliacao_pk"))
        # Retorna a avaliação com o id informado (avaliacao_pk).
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("avaliacao_pk"))


"""
API version 2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=["get"])
    def avaliacoes(self, request, pk=None):
        # Busca o curso pelo id informado na URL (pk).
        curso = self.get_object()
        # Busca todas as avaliações do curso encontrado.
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
