import cProfile
from socket import NI_NUMERICHOST
from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.utils import timezone

CHOICES = (
    ('S','Sim'),
    ('N','Não')
)

class Aluno(models.Model):
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    imc = models.DecimalField(default=20, decimal_places=2, max_digits=3)
    posicao = models.CharField(max_length=10)
    possuiProblemaSaude = models.CharField(choices=CHOICES, max_length=2)
    altura = models.DecimalField(default=1.70, decimal_places=2, max_digits=3)
    massa = models.DecimalField(default=70, decimal_places=3, max_digits=6)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=35)
    dataNascimento = models.DateField()
    idade = models.CharField(default=10, max_length=2)
    qualProblema = models.CharField(max_length=50)
    observacao = models.TextField(max_length=255)
    foto = models.ImageField()

class Responsavel(models.Model):
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    dataNascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=30)

class Professor(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    observacoes = models.TextField(max_length=255)

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    textoPadrao = models.TextField()
    telefone = models.CharField(max_length=15)
    contato1 = models.CharField(max_length=60)
    contato2 = models.CharField(max_length=60)
    contato3 = models.CharField(max_length=60)
    logo = models.ImageField()

class Escola(models.Model):
    nome = models.CharField(max_length=100)
    serie = models.CharField(max_length=2)
    turno = models.CharField(max_length=1)

class Valores(models.Model):
    descricao = models.CharField(max_length=15)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

class Ficha(models.Model):
    data = models.DateField()
    comoSoube = models.CharField(max_length=15)
    formaPagamento = models.CharField(max_length=10)
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    responsavel_id = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    escola_id = models.ForeignKey(Escola, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    valores_id = models.ForeignKey(Valores, on_delete=models.CASCADE)
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Financeiro(models.Model):
    tipoMovimento = models.CharField(max_length=1)
    dataMovimento = models.DateTimeField()
    valorPago = models.DecimalField(max_digits=7, decimal_places=2)
    situacao = models.CharField(max_length=1)
    ficha_id = models.ForeignKey(Ficha, on_delete=models.CASCADE)

class Chamada(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=255)
    ficha_id = models.ForeignKey(Ficha, on_delete=models.CASCADE)