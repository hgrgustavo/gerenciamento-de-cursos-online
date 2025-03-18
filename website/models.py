from django.db import models


class Administrador(models.Model):
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'administrador'


class Alunos(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    telefone = models.CharField(max_length=18)

    class Meta:
        
        db_table = 'alunos'


class Cursos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    instrutor = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'cursos'


class Inscricoes(models.Model):
    cursos = models.ForeignKey(Cursos, models.DO_NOTHING)
    alunos = models.ForeignKey(Alunos, models.DO_NOTHING)

    class Meta:
        
        db_table = 'inscricoes'
