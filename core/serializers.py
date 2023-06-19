from rest_framework import routers, serializers, viewsets
from .models import *

class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ('cpf', 'rg', 'posicao', 'possuiProblemaSaude', 'altura', 'massa', 'imc', 'nome', 'sobrenome', 'dataNascimento', 'qualProblema', 'observacao', 'foto')