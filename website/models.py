from django.db import models


class Alunos(models.Model):
    nome = models.CharField(max_length=255, default="")
    email = models.CharField(unique=True, max_length=255, default="")
    telefone = models.CharField(max_length=18, default="")

    class Meta:
        
        db_table = 'alunos'


class Cursos(models.Model):
    nome = models.CharField(max_length=255, default="")
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    instrutor = models.CharField(max_length=255, default="")

    class Meta:
        
        db_table = 'cursos'


class Inscricoes(models.Model):
    cursos = models.ForeignKey(Cursos, models.DO_NOTHING)
    alunos = models.ForeignKey(Alunos, models.DO_NOTHING)

    class Meta:
        
        db_table = 'inscricoes'
        unique_together = (('cursos', 'alunos'),)
