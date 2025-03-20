from django.db import models
from django.contrib.auth import hashers


class Usuario(models.Model):
    TIPOS_USUARIO = [
        ("admin", "Administrador"),
        ("aluno", "Aluno"),
    ]

    nome = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255, default="")
    telefone = models.CharField(unique=True, max_length=18, default="")
    _senha = models.CharField(max_length=255, default="", editable="false")
    tipo_usuario = models.CharField(
        choices=TIPOS_USUARIO, max_length=20, default="")

    def save(self, *args, **kwargs):
        if self.senha:
            self.senha = hashers.make_password(
                self.senha, salt=None, hasher=hashers.ScryptPasswordHasher)
        super().save(*args, **kwargs)

    def check_senha(self, senha):
        return hashers.check_password(senha, self.senha)

    @property
    def senha(self):
        return AttributeError("Não pode ser acessado diretamente.")

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
