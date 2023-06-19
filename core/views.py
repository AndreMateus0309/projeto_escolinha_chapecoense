from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .serializers import AlunoSerializer

# Generico

def index(request):
    num_alunos = Aluno.objects.all().count()
    num_professores = Professor.objects.all().count
    context = {
        'num_alunos' : num_alunos,
        'num_professores' : num_professores
    }
    template_name = 'home.html'
    return render(request, template_name, context) 

# Aluno

class listaAlunos(ListView):
    template_name = 'listaAlunos.html'
    context_object_name = 'alunos_list'

    def get_queryset(self):
        return Aluno.objects.all()
    
def inadimplentes(request):
    alunos = Aluno.objects.all()
    fichas = Ficha.objects.all()
    inadimplentes = []

class detalhesAluno(DetailView):
    model = Aluno
    template_name ='detalhesAluno.html'

def cadastroAluno(request):
    form = AlunoForm()
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            return redirect('DetalhesAluno', aluno.pk)
    return render(request,'cadastro.html',{'form': form})

def editarAluno(request, pk, template_name='cadastro.html'):
    alunos = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=alunos)
    if form.is_valid():
        form.save()
        return redirect('DetalhesAluno', pk)
    return render(request, template_name, {'form':form})

def excluirAluno(request, pk, template_name='confirm_delete.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('ListaAlunos')
    return render(request, template_name, {'object':aluno})

# Responsavel

class listaResponsavel(ListView):
    template_name = 'listaResponsavel.html'
    context_object_name = 'responsavel_list'

    def get_queryset(self):
        return Responsavel.objects.all()

class detalhesResponsavel(DetailView):
    model = Responsavel
    template_name ='detalhesResponsavel.html'

def cadastroResponsavel(request):
    if request.method == 'POST':
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaResponsavel')
    form = ResponsavelForm()

    return render(request,'cadastro.html',{'form': form})

def editarResponsavel(request, pk, template_name='cadastro.html'):
    responsavel = get_object_or_404(Responsavel, pk=pk)
    form = ResponsavelForm(request.POST or None, instance=responsavel)
    if form.is_valid():
        form.save()
        return redirect('ListaResponsavel')
    return render(request, template_name, {'form':form})

def excluirResponsavel(request, pk, template_name='confirm_delete.html'):
    responsavel = get_object_or_404(Responsavel, pk=pk)
    if request.method=='POST':
        responsavel.delete()
        return redirect('ListaResponsavel')
    return render(request, template_name, {'object':responsavel})

# Professor

class listaProfessor(ListView):
    template_name = 'listaProfessor.html'
    context_object_name = 'professor_list'

    def get_queryset(self):
        return Professor.objects.all()

class detalhesProfessor(DetailView):
    model = Professor
    template_name ='detalhesProfessor.html'

def cadastroProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaProfessor')
    form = ProfessorForm()

    return render(request,'cadastro.html',{'form': form})

def editarProfessor(request, pk, template_name='cadastro.html'):
    professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('ListaProfessor')
    return render(request, template_name, {'form':form})

def excluirProfessor(request, pk, template_name='confirm_delete.html'):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method=='POST':
        professor.delete()
        return redirect('ListaProfessor')
    return render(request, template_name, {'object':professor})

#Valores

class listaValores(ListView):
    template_name = 'listaValores.html'
    context_object_name = 'valores_list'

    def get_queryset(self):
        return Valores.objects.all()

class detalhesValores(DetailView):
    model = Valores
    template_name ='detalhesValores.html'

def cadastroValores(request):
    if request.method == 'POST':
        form = ValoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaValores')
    form = ValoresForm()

    return render(request,'cadastro.html',{'form': form})

def editarValores(request, pk, template_name='cadastro.html'):
    valores = get_object_or_404(Valores, pk=pk)
    form = FinanceiroForm(request.POST or None, instance=valores)
    if form.is_valid():
        form.save()
        return redirect('ListaValores')
    return render(request, template_name, {'form':form})

def excluirValores(request, pk, template_name='confirm_delete.html'):
    valores = get_object_or_404(Valores, pk=pk)
    if request.method=='POST':
        valores.delete()
        return redirect('ListaValores')
    return render(request, template_name, {'object':valores})

#Financeiro

class listaFinanceiro(ListView):
    template_name = 'listaFinanceiro.html'
    context_object_name = 'financeiro_list'

    def get_queryset(self):
        return Financeiro.objects.all()

class detalhesFinanceiro(DetailView):
    model = Financeiro
    template_name ='detalhesFinanceiro.html'

def cadastroFinanceiro(request):
    if request.method == 'POST':
        form = FinanceiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaFinanceiro')
    form = FinanceiroForm()

    return render(request,'cadastro.html',{'form': form})

def editarFinanceiro(request, pk, template_name='cadastro.html'):
    financeiro = get_object_or_404(Financeiro, pk=pk)
    form = FinanceiroForm(request.POST or None, instance=financeiro)
    if form.is_valid():
        form.save()
        return redirect('ListaFinanceiro')
    return render(request, template_name, {'form':form})

def excluirFinanceiro(request, pk, template_name='confirm_delete.html'):
    financeiro = get_object_or_404(Financeiro, pk=pk)
    if request.method=='POST':
        financeiro.delete()
        return redirect('ListaFinanceiro')
    return render(request, template_name, {'object':financeiro})

#Chamada

class listaChamada(ListView):
    template_name = 'listaChamada.html'
    context_object_name = 'chamada_list'

    def get_queryset(self):
        return Chamada.objects.all()

class detalhesChamada(DetailView):
    model = Chamada
    template_name ='detalhesChamada.html'

def cadastroChamada(request):
    if request.method == 'POST':
        form = ChamadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaChamada')
    form = ChamadaForm()

    return render(request,'cadastro.html',{'form': form})

def editarChamada(request, pk, template_name='cadastro.html'):
    chamada = get_object_or_404(Chamada, pk=pk)
    form = ChamadaForm(request.POST or None, instance=chamada)
    if form.is_valid():
        form.save()
        return redirect('ListaChamada')
    return render(request, template_name, {'form':form})

def excluirChamada(request, pk, template_name='confirm_delete.html'):
    chamada = get_object_or_404(Chamada, pk=pk)
    if request.method=='POST':
        chamada.delete()
        return redirect('ListaChamada')
    return render(request, template_name, {'object':chamada})

#Ficha

class listaFicha(ListView):
    template_name = 'listaFicha.html'
    context_object_name = 'fichas_list'

    def get_queryset(self):
        return Ficha.objects.all()

class detalhesFicha(DetailView):
    model = Ficha
    template_name ='detalhesFicha.html'

def cadastroFicha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaFicha')
    form = FichaForm()

    return render(request,'cadastro.html',{'form': form})

def editarFicha(request, pk, template_name='cadastro.html'):
    ficha = get_object_or_404(Ficha, pk=pk)
    form = FichaForm(request.POST or None, instance=ficha)
    if form.is_valid():
        form.save()
        return redirect('ListaFicha')
    return render(request, template_name, {'form':form})

def excluirFicha(request, pk, template_name='confirm_delete.html'):
    ficha = get_object_or_404(Ficha, pk=pk)
    if request.method=='POST':
        ficha.delete()
        return redirect('ListaFicha')
    return render(request, template_name, {'object':ficha})

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
