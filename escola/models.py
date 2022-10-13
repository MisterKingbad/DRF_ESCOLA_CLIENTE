from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=150) #Campos
    rg = models.CharField(max_length=9) #Campos
    cpf = models.CharField(max_length=11) #Campos
    data_nascimento = models.DateField() #Campos
    celular = models.CharField(max_length=11, blank=True, null=True) #Campos

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado')
    )
    codigo_curso = models.CharField(max_length=10)
    descrisao_curso = models.CharField(max_length=150)
    nivel_curso = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='B')

    def __str__(self):
        return self.descrisao_curso


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False,default='M')
