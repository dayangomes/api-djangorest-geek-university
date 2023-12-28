from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos da Geek University
    """

    def get(self, request):
        cursos = Curso.objects.all()
        # many=True para retornar uma lista de objetos
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # data=request.data para pegar os dados enviados pelo usuário
        serializer = CursoSerializer(data=request.data)
        # Se não for válido, retorna um erro
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Salva os dados no banco de dados
        return Response({"mensagem": "Curso criado com sucesso!", "dados": serializer.data}, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliações da Geek University
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        # many=True para retornar uma lista de objetos
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        # data=request.data para pegar os dados enviados pelo usuário
        serializer = AvaliacaoSerializer(data=request.data)
        # Se não for válido, retorna um erro
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Salva os dados no banco de dados
        return Response({"mensagem": "Avaliação criada com sucesso!", "dados": serializer.data}, status=status.HTTP_201_CREATED)
