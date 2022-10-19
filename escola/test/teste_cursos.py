from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
class CursoTestcase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1' , descrisao_curso='Curso teste', nivel_curso='B'
            )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2' , descrisao_curso='Curso teste 2', nivel_curso='I'
            )
        
    # def test_falhador(self):
    #     self.fail('Teste falhador')
    
    def test_requisicao_get_para_listar_cursos(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
        
    def test_requisicao_post_para_criar_curso(self):
        data = {
            'codigo_curso':'CTT3', 'descrisao_curso':'Curso teste 3', 'nivel_curso':'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)