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
    media_avaliacoes = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)  # Nota de 0 a 5

    class Meta:
        verbose_name_plural = 'Cursos'
        verbose_name = 'Curso'
        ordering = ['id']  # Ordena por id

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Faz a média das avaliações do curso
        avaliacoes = Avaliacao.objects.filter(curso_id=self.id)
        if avaliacoes:
            media = avaliacoes.aggregate(
                models.Avg('avaliacao')).get('avaliacao__avg')
            self.media_avaliacoes = round(media * 2) / 2
        else:
            self.media_avaliacoes = None
        super(Curso, self).save(*args, **kwargs)


class Avaliacao(Base):
    # Relacionamento com a tabela Curso
    curso = models.ForeignKey(
        Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(
        max_digits=2, decimal_places=1)  # Nota de 0 a 10

    class Meta:
        verbose_name_plural = 'Avaliações'
        verbose_name = 'Avaliação'
        unique_together = ['email', 'curso']  # Não permite avaliação duplicada
        ordering = ['id']  # Ordena por id

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'

    # def save(self, *args, **kwargs):
    #     super(Avaliacao, self).save(*args, **kwargs)
    #     # Faz a média das avaliações do curso
    #     curso = Curso.objects.get(id=self.curso.id)
    #     avaliacoes = Avaliacao.objects.filter(curso_id=curso.id)
    #     media = avaliacoes.aggregate(models.Avg('avaliacao')).get('avaliacao__avg')
    #     curso.media_avaliacoes = round(media * 2) / 2
    #     curso.save()
