from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}  # Não exibe o email
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship, trabalha com o objeto
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field, trabalha com a url do objeto
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field, trabalha com o id do objeto
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
