import cProfile
from django.conf import settings
from django.db import models
from datetime import date
from django_cpf_cnpj.fields import CNPJField, CPFField

COMO_SOUBE_CHOICES = (
    ('I', 'Internet'),
    ('J', 'Jornal'),
    ('R', 'Rádio'),
    ('O', 'Outros')
)

POSICAO_CHOICES = (
    ('GO', 'Goleiro'),
    ('LD', 'Lateral Direito'),
    ('LE', 'Lateral Esquerdo'),
    ('ZC', 'Zagueiro'),
    ('VOL', 'Volante'),
    ('MLG', 'Meia de Ligação'),
    ('MLD', 'Meia de Ligação Direita'),
    ('MLE', 'Meia de Ligação Esquerda'),
    ('MAT', 'Meia Atacante'),
    ('PTE', 'Ponta Esquerda'),
    ('PTD', 'Ponta Direita'),
    ('CA', 'Centroavante'),
)

CHOICES = (
    ('S','Sim'),
    ('N','Não')
)

TIPO_MOVIMENTO = (
    ('P','Pix'),
    ('D','Dinheiro'),
    ('O','Outro')
)

SITUACAO_FINANCEIRO = (
    ('0','OK'),
    ('1','Inadimplente')
)

VALORES_PADRAO = (
    (50.00, 'R$50,00'),
    (100.00, 'R$100,00'),
    (150.00, 'R$150,00'),
    (200.00, 'R$200,00'),
    (250.00, 'R$250,00'),
    (300.00, 'R$300,00'),
)

class Aluno(models.Model):
    cpf = CPFField(masked=True)
    rg = models.CharField(max_length=20)
    posicao = models.CharField(choices = POSICAO_CHOICES, max_length=10)
    possuiProblemaSaude = models.CharField(choices=CHOICES, max_length=2)
    altura = models.IntegerField()
    massa = models.IntegerField()
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=35)
    dataNascimento = models.DateField()
    qualProblema = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.TextField(max_length=255, blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.nome) + " - " + str(self.cpf) + " - " + str(self.dataNascimento)
    
    @property
    def imc(self):
        imc = ((self.massa) / (self.altura*self.altura)) * 10000
        return imc


class Responsavel(models.Model):
    cpf = CPFField(masked=True)
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    dataNascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=30)

    def __str__(self):
        return str(self.nome) + " - " + str(self.cpf) + " - " + str(self.dataNascimento)

class Professor(models.Model):
    cpf = CPFField(masked=True)
    nome = models.CharField(max_length=50)
    observacoes = models.TextField(max_length=255)

    def __str__(self):
        return str(self.nome) + " - " + str(self.cpf) + " - " + str(self.observacoes)

class Valores(models.Model):
    descricao = models.CharField(max_length=15)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.descricao) + " - " + str(self.preco)
    
class Ficha(models.Model):
    data = models.DateField()
    comoSoube = models.CharField(choices = COMO_SOUBE_CHOICES, max_length=15)
    formaPagamento = models.CharField(max_length=10)
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    responsavel_id = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    valores_id = models.ForeignKey(Valores, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.data) + " - " + str(self.aluno_id.nome) + " - " + str(self.aluno_id.cpf)

class Financeiro(models.Model):
    tipoMovimento = models.CharField(choices=TIPO_MOVIMENTO, max_length=1)
    dataMovimento = models.DateField()
    valorPago = models.DecimalField(choices=VALORES_PADRAO, max_digits=7, decimal_places=2)
    situacao = models.CharField(choices=SITUACAO_FINANCEIRO, max_length=1)
    ficha_id = models.ForeignKey(Ficha, on_delete=models.CASCADE)

class Chamada(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=255)
    ficha_id = models.ForeignKey(Ficha, on_delete=models.CASCADE)
