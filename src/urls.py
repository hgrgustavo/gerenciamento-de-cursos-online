
# from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="homepage"),
    path("admin/", views.AdminView.as_view(), name="adminpage"),
    path("cursos/", views.CoursesView.as_view(), name="coursespage"),

    path("admin/adicionar-aluno/", views.AdminCreateStudent.as_view(),
         name="admincreatestudentpage"),

    path("admin/adicionar-curso/", views.AdminCreateCourse.as_view(),
         name="admincreatecoursepage"),

    path("admin/listar-alunos/", views.AdminListStudents.as_view(),
         name="adminliststudentspage"),

    path("admin/listar-cursos/", views.AdminListCourses.as_view(),
         name="adminlistcoursespage"),

    path("admin/listar-alunos/excluir/<int:pk>/",
         views.AdminDeleteStudent.as_view(), name="admindeletestudentpage"),

    path("admin/listar-cursos/excluir/<int:pk>/",
         views.AdminDeleteCourses.as_view(), name="admindeletecoursepage"),

    path("cursos/ingressar/<int:pk>/",
         views.CreateEnrollment.as_view(), name="createenrollmentpage"),

    path("admin/listar-alunos/alterar/<int:pk>/",
         views.AdminUpdateStudent.as_view(), name="adminupdatestudentpage"),

    path("admin/listar-cursos/alterar/<int:pk>/",
         views.AdminUpdateCourse.as_view(), name="adminupdatecoursepage"),






]
