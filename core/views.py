from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView

# Generico

def index(request):
    num_alunos = Aluno.objects.all().count()
    num_professores = Professor.objects.all().count
    num_escolas = Escola.objects.all().count
    context = {
        'num_alunos' : num_alunos,
        'num_professores' : num_professores,
        'num_escolas' : num_escolas
    }
    template_name = 'login.html'
    return render(request, template_name, context) 

# Aluno

class listaAlunos(ListView):
    template_name = 'listaAlunos.html'
    context_object_name = 'alunos_list'

    def get_queryset(self):
        return Aluno.objects.all()    

class detalhesAluno(DetailView):
    model = Aluno
    template_name ='detalhesAluno.html'

def cadastroAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Aluno')
    form = AlunoForm()

    return render(request,'cadastrarAluno.html',{'form': form})

def editarAluno(request, pk, template_name='editarAluno.html'):
    alunos = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=alunos)
    if form.is_valid():
        form.save()
        return redirect('Aluno')
    return render(request, template_name, {'form':form})

def excluirAluno(request, pk, template_name='excluirAluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('Aluno')
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
            return redirect('Responsavel')
    form = ResponsavelForm()

    return render(request,'cadastrarResponsavel.html',{'form': form})

def editarResponsavel(request, pk, template_name='editarResponsavel.html'):
    responsavel = get_object_or_404(Responsavel, pk=pk)
    form = ResponsavelForm(request.POST or None, instance=responsavel)
    if form.is_valid():
        form.save()
        return redirect('Responsavel')
    return render(request, template_name, {'form':form})

def excluirResponsavel(request, pk, template_name='excluirResponsavel.html'):
    responsavel = get_object_or_404(Responsavel, pk=pk)
    if request.method=='POST':
        responsavel.delete()
        return redirect('Responsavel')
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
            return redirect('Professor')
    form = ProfessorForm()

    return render(request,'cadastrarProfessor.html',{'form': form})

def editarProfessor(request, pk, template_name='editarProfessor.html'):
    professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('Professor')
    return render(request, template_name, {'form':form})

def excluirProfessor(request, pk, template_name='excluirProfessor.html'):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method=='POST':
        professor.delete()
        return redirect('Professor')
    return render(request, template_name, {'object':professor})

# Empresa

class listaEmpresa(ListView):
    template_name = 'listaEmpresa.html'
    context_object_name = 'empresa_list'

    def get_queryset(self):
        return Empresa.objects.all()

def cadastroEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Empresa')
    form = EmpresaForm()

    return render(request,'cadastrarEmpresa.html',{'form': form})

# Escola

class listaEscola(ListView):
    template_name = 'listaEscola.html'
    context_object_name = 'escola_list'

    def get_queryset(self):
        return Escola.objects.all()

def cadastroEscola(request):
    if request.method == 'POST':
        form = EscolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Escola')
    form = EscolaForm()

    return render(request,'cadastrarEscola.html',{'form': form})

def editarEscola(request, pk, template_name='editarEscola.html'):
    escola = get_object_or_404(Escola, pk=pk)
    form = FinanceiroForm(request.POST or None, instance=escola)
    if form.is_valid():
        form.save()
        return redirect('Escola')
    return render(request, template_name, {'form':form})

def excluirEscola(request, pk, template_name='excluirEscola.html'):
    escola = get_object_or_404(Escola, pk=pk)
    if request.method=='POST':
        escola.delete()
        return redirect('Escola')
    return render(request, template_name, {'object':escola})

#Valores

class listaValores(ListView):
    template_name = 'listaValores.html'
    context_object_name = 'valores_list'

    def get_queryset(self):
        return Valores.objects.all()

def cadastroValores(request):
    if request.method == 'POST':
        form = ValoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Valores')
    form = ValoresForm()

    return render(request,'cadastrarValores.html',{'form': form})

def editarValores(request, pk, template_name='editarValores.html'):
    valores = get_object_or_404(Valores, pk=pk)
    form = FinanceiroForm(request.POST or None, instance=valores)
    if form.is_valid():
        form.save()
        return redirect('Valores')
    return render(request, template_name, {'form':form})

def excluirValores(request, pk, template_name='excluirValores.html'):
    valores = get_object_or_404(Valores, pk=pk)
    if request.method=='POST':
        valores.delete()
        return redirect('Valores')
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
            return redirect('Financeiro')
    form = FinanceiroForm()

    return render(request,'cadastrarFinanceiro.html',{'form': form})

def editarFinanceiro(request, pk, template_name='editarFinanceiro.html'):
    financeiro = get_object_or_404(Financeiro, pk=pk)
    form = FinanceiroForm(request.POST or None, instance=financeiro)
    if form.is_valid():
        form.save()
        return redirect('Financeiro')
    return render(request, template_name, {'form':form})

def excluirFinanceiro(request, pk, template_name='excluirFinanceiro.html'):
    financeiro = get_object_or_404(Financeiro, pk=pk)
    if request.method=='POST':
        financeiro.delete()
        return redirect('Financeiro')
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
            return redirect('Chamada')
    form = ChamadaForm()

    return render(request,'cadastrarChamada.html',{'form': form})

def editarChamada(request, pk, template_name='editarChamada.html'):
    chamada = get_object_or_404(Chamada, pk=pk)
    form = ChamadaForm(request.POST or None, instance=chamada)
    if form.is_valid():
        form.save()
        return redirect('Chamada')
    return render(request, template_name, {'form':form})

def excluirChamada(request, pk, template_name='excluirChamada.html'):
    chamada = get_object_or_404(Chamada, pk=pk)
    if request.method=='POST':
        chamada.delete()
        return redirect('Chamada')
    return render(request, template_name, {'object':chamada})

#Ficha

class listaFicha(ListView):
    template_name = 'listaFicha.html'
    context_object_name = 'ficha_list'

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
            return redirect('Ficha')
    form = FichaForm()

    return render(request,'cadastrarFicha.html',{'form': form})

def editarFicha(request, pk, template_name='editarFicha.html'):
    ficha = get_object_or_404(Ficha, pk=pk)
    form = FichaForm(request.POST or None, instance=ficha)
    if form.is_valid():
        form.save()
        return redirect('Ficha')
    return render(request, template_name, {'form':form})

def excluirFicha(request, pk, template_name='excluirFicha.html'):
    ficha = get_object_or_404(Ficha, pk=pk)
    if request.method=='POST':
        ficha.delete()
        return redirect('Ficha')
    return render(request, template_name, {'object':ficha})
