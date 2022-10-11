from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewsSet, CursosViewset, MatriculasViewsSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewsSet, basename=' Alunos')
router.register('cursos', CursosViewset, basename='Cursos')
router.register('matriculas', MatriculasViewsSet, basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaAlunosMatriculados.as_view())
]
