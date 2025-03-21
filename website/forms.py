from django import forms
from . import models


class AdminCreateStudentForm(forms.ModelForm):
    class Meta:
        model = models.Aluno
        exclude = [
            "tipo_usuario",
        ]
        fields = [
            "nome",
            "email",
            "senha",
            "telefone",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control mx-2", "id": "inputName"}),
            "email": forms.EmailInput(attrs={"class": "form-control mx-2", "id": "inputEmail"}),
            "telefone": forms.TextInput(attrs={"class": "form-control mx-2", "id": "inputPhone"}),
            "senha": forms.PasswordInput(attrs={"class": "form-control mx-2", "id": "inputPassword"}),
        }


class AdminCreateCourseForm(forms.ModelForm):
    class Meta:
        model = models.Cursos
        fields = [
            "nome",
            "descricao",
            "carga_horaria",
            "instrutor",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control mx-2", "id": "inputCourseName"}),
            "descricao": forms.Textarea(attrs={"class": "form-control mx-2", "id": "inputCourseDescription"}),
            "carga_horaria": forms.NumberInput(attrs={"class": "form-control mx-2", "id": "inputCourseHour"}),
            "instrutor": forms.TextInput(attrs={"class": "form-control mx-2", "id": "inputCourseInstructor"}),
        }
