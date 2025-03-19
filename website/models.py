from django.db import models 
from django.contrib.auth.hashers import make_password, ScryptPasswordHasher


class Usuario(models.Model):
    def save(self, *args, **kwargs):
        if self.senha:
            self.senha = make_password(self.senha, salt=None, hasher=ScryptPasswordHasher)


    TIPOS_USUARIO = {
        "admin": "Administrador",
        "aluno": "Aluno",
    }

    nome = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255, default="")
    telefone = models.CharField(unique=True, max_length=18, default="")
    senha = models.CharField(max_length=30, default="")
    tipo_usuario = models.CharField(choices=TIPOS_USUARIO, max_length=20, default="")

    class Meta: 
        abstract = True
        db_table = 'usuario'
  
 
class Administrador(Usuario):
    def save(self, *args, **kwargs):
        self.tipo_usuario = "admin"
        super().save(*args, **kwargs)
        
    class Meta:
        db_table = 'administrador'


class Aluno(Usuario):
    def save(self, *args, **kwargs):
        self.tipo_usuario = "aluno"
        super().save(*args, **kwargs)
     
    class Meta:
        db_table = 'aluno'


class Cursos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    instrutor = models.CharField(max_length=255)

    class Meta: 
        db_table = 'cursos'


class Inscricoes(models.Model):
    cursos = models.ForeignKey(Cursos, models.DO_NOTHING)
    aluno = models.ForeignKey(Aluno, models.DO_NOTHING, default="")

    class Meta:
        db_table = 'inscricoes'
