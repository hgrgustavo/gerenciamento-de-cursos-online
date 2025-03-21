
from django.views.generic import base, edit, list
from . import models, forms
from django import http
from django.views.decorators import csrf
from django.utils import decorators


class HomeView(base.TemplateView):
    template_name = "index.html"


class AdminView(base.TemplateView):
    template_name = "admin.html"


class CoursesView(base.TemplateView):
    template_name = "courses.html"


# create
class AdminCreateStudent(edit.CreateView):
    template_name = "admin_createstudent.html"
    model = models.Aluno
    form_class = forms.AdminCreateStudentForm
    success_url = "#"


class AdminCreateCourse(edit.CreateView):
    template_name = "admin_createcourse.html"
    model = models.Cursos
    form_class = forms.AdminCreateCourseForm
    success_url = "#"


# read
decorators.method_decorator(csrf.csrf_exempt, name="dispatch")


class AdminListStudents(list.ListView):
    template_name = "admin_readstudents.html"
    model = models.Aluno
    context_object_name = "alunos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AdminListCourses(list.ListView):
    template_name = "admin_readcourses.html"
    model = models.Cursos
    context_object_name = "cursos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ListCourses(list.ListView):
    template_name = "courses_read"
    model = models.Cursos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# delete
class AdminDeleteStudent(edit.DeleteView):
    def post(self, request, *args, **kwargs):
        try:
            student_id = kwargs.get("pk")
            student_object = models.Aluno.objects.get(pk=student_id)
            student_object.delete()

            return http.JsonResponse({"success": True})

        except models.Aluno.DoesNotExist:
            return http.JsonResponse({"success": False, "error": "Item not found"})


class AdminDeleteCourses(edit.DeleteView):
    def post(self, request, *args, **kwargs):
        try:
            course_id = kwargs.get("pk")
            course_object = models.Cursos.objects.get(pk=course_id)
            course_object.delete()

            return http.JsonResponse({"success": True})

        except models.Cursos.DoesNotExist:
            return http.JsonResponse({"success": False, "error": "Item not found"})
