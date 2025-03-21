# Generated by Django 5.1.7 on 2025-03-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('senha', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'administrador',
            },
        ),
        migrations.AlterUniqueTogether(
            name='inscricoes',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='telefone',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='instrutor',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
