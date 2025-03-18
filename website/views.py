from django.shortcuts import render
from django.views.generic.edit import CreateView 
from . import models, forms


class CreateCursoView(CreateView):
    template_name = "create_curso.html"
    model = models.Curso 
    form_class = forms.CreateCursoForm
    success_url = "#"