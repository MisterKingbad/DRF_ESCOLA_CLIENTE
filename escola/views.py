from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer,ListaAlunoMatriculadosSerializer
from rest_framework.response import Response

class AlunosViewsSet(viewsets.ModelViewSet):
        """Exibindo todos os alunas e alunas"""
        queryset = Aluno.objects.all()
        def get_serializer_class(self):
                if self.request.version == 'v2':
                        return AlunoSerializerV2
                else:
                        return AlunoSerializer

class CursosViewset(viewsets.ModelViewSet):
        """Ëxibindo todos os cursos"""
        queryset = Curso.objects.all()
        serializer_class = CursoSerializer
        
        def create(self, request): 
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        response = Response(serializer.data, status=status.HTTP_201_CREATED)
                        id = str(serializer.data['id'])
                        response['Location'] = request.build_absolute_uri() + id
                        return response

class MatriculasViewsSet(viewsets.ModelViewSet):
        """Exibindo todas as matriculas"""
        queryset = Matricula.objects.all()
        serializer_class = MatriculaSerializer
        http_method_names = ['get', 'post', 'put', 'path'] #Métodos que serão exibidos

class ListaMatriculasAluno(generics.ListAPIView):
        """Listando as matriculas de um aluno(a)"""
        def get_queryset(self):
                queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
                return queryset
        serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
        """Listando alunos(as) matriculados em um curso"""
        def get_queryset(self):
                queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
                return queryset
        serializer_class = ListaAlunoMatriculadosSerializer
        