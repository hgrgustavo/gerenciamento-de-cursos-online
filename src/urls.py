
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
     
     # path("cursos/listar-cursos/", views.ListCourses.as_view(),
     #      name="courseslistpage")






]
