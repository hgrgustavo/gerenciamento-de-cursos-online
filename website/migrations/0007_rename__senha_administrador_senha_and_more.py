# Generated by Django 5.1.7 on 2025-03-21 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_administrador__senha_alter_aluno__senha'),
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
