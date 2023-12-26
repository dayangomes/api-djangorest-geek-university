from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name_plural = 'Cursos'
        verbose_name = 'Curso'
        ordering = ['titulo'] # Ordena por título

    def __str__(self):
        return self.titulo

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE) # Relacionamento com a tabela Curso
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1) # Nota de 0 a 10

    class Meta:
        verbose_name_plural = 'Avaliações'
        verbose_name = 'Avaliação'
        unique_together = ['email', 'curso'] # Não permite avaliação duplicada
        ordering = ['-avaliacao'] # Ordena por avaliação

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
