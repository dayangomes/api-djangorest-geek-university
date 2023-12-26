from django.contrib import admin

from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao',
                    'ativo')  # Campos que serão exibidos na listagem
    list_filter = ('titulo', 'criacao', 'atualizacao',
                   'ativo')  # Campos que serão filtrados
    search_fields = ('titulo',)  # Campos que serão pesquisados


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao',
                    'criacao', 'atualizacao', 'ativo')
