
from django.views.generic import base, edit, list
from . import models, forms


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
class AdminListStudents(list.ListView):
    template_name = "admin_readstudents.html"
    model = models.Aluno

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AdminListCourses(list.ListView):
    template_name = "admin_readcourses.html"
    model = models.Cursos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
