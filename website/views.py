
from django.views.generic import base, edit, list
from . import models, forms
from django import http


class HomeView(base.TemplateView):
    template_name = "index.html"


class AdminView(base.TemplateView):
    template_name = "admin.html"


class CoursesView(list.ListView):
    template_name = "courses.html"
    model = models.Cursos
    context_object_name = "courses"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


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


class CreateEnrollment(edit.CreateView):
    template_name = "courses_createenrollment.html"
    model = models.Inscricoes
    form_class = forms.CreateEnrollmentForm
    success_url = "#"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_pk = self.kwargs.get('pk')

        if course_pk:
            try:
                context["course_name"] = models.Cursos.objects.get(
                    pk=course_pk).nome

            except models.Cursos.DoesNotExist:
                context["course_name"] = "Curso não encontrado"

        return context


# read
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


class AdminUpdateStudent(edit.UpdateView):
    template_name = "admin_updatestudent.html"
    model = models.Aluno
    form_class = forms.AdminUpdateStudentForm


class AdminUpdateCourse(edit.UpdateView):
    template_name = "admin_updatecourse.html"
    model = models.Cursos
    form_class = forms.AdminUpdateCourseForm
