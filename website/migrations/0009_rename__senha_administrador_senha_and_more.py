# Generated by Django 5.1.7 on 2025-03-21 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_administrador_senha_remove_aluno_senha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='_senha',
            new_name='senha',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='_senha',
            new_name='senha',
        ),
    ]
