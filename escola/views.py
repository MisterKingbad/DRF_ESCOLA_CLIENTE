from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer,ListaAlunoMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class AlunosViewsSet(viewsets.ModelViewSet):
        """Exibindo todos os alunas e alunas"""
        queryset = Aluno.objects.all()
        authentication_classes = [BasicAuthentication]
        def get_serializer_class(self):
                if self.request.version == 'v2':
                        return AlunoSerializerV2
                else:
                        return AlunoSerializer

class CursosViewset(viewsets.ModelViewSet):
        """Ëxibindo todos os cursos"""
        queryset = Curso.objects.all()
        serializer_class = CursoSerializer
        authentication_classes = [BasicAuthentication]

class MatriculasViewsSet(viewsets.ModelViewSet):
        """Exibindo todas as matriculas"""
        queryset = Matricula.objects.all()
        serializer_class = MatriculaSerializer
        authentication_classes = [BasicAuthentication]

class ListaMatriculasAluno(generics.ListAPIView):
        """Listando as matriculas de um aluno(a)"""
        def get_queryset(self):
                queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
                return queryset
        serializer_class = ListaMatriculasAlunoSerializer
        authentication_classes = [BasicAuthentication]

class ListaAlunosMatriculados(generics.ListAPIView):
        """Listando alunos(as) matriculados em um curso"""
        def get_queryset(self):
                queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
                return queryset
        serializer_class = ListaAlunoMatriculadosSerializer
        authentication_classes = [BasicAuthentication]
        