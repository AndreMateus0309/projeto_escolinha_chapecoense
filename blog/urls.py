from django.urls import path
from blog import views

#Generic
urlpatterns = [
    path('home/', views.index, name='home')
]

#Aluno
urlpatterns += [
    path('listaralunos/', views.listaAlunos, name='ListaAlunos'),
    path('alunos/cadastraraluno', views.cadastroAluno, name='CadastroAlunos'),
    path('aluno/<int:pk>', views.detalhesAluno.as_view(), name='DetalhesAluno'),
    path('aluno/editar/<int:pk>', views.editarAluno, name='EditarAluno'),
    path('aluno/deletar/<int:pk>', views.excluirAluno, name='ExcluirAluno')
]

#Responsavel
urlpatterns += [
    path('listarresponsavel/', views.listaResponsavel.as_view(), name='ListaResponsavel'),
    path('responsavel/cadastrarresponsavel', views.cadastroResponsavel, name='CadastroResponsavel'),
    path('aluno/<int:pk>', views.detalhesResponsavel.as_view(), name='DetalhesResponsavel'),
    path('aluno/editar/<int:pk>', views.editarResponsavel, name='EditarResponsavel'),
    path('aluno/deletar/<int:pk>', views.excluirResponsavel, name='ExcluirAluno')
]

#Professor
urlpatterns += [
    path('professor/', views.listaProfessor.as_view(), name='ListaProfessor'),
    path('professor/cadastrarprofessor', views.cadastroProfessor, name='CadastroProfessor'),
    path('professor/<int:pk>', views.detalhesProfessor, name='DetalhesProfessor'),
    path('professor/editar/<int:pk>', views.editarProfessor, name='EditarProfessor'),
    path('professor/deletar/<int:pk>', views.excluirProfessor, name='ExcluirProfessor')
]

#Empresa
urlpatterns += [
    path('empresa/', views.listaEmpresa.as_view(), name='ListaEmpresa'),
    path('empresa/cadastrarempresa', views.cadastroEmpresa, name='CadastroEmpresa')
]

#Escola
urlpatterns += [
    path('escola/', views.listaEscola.as_view(), name='ListaEscola'),
    path('escola/cadastrarescola', views.cadastroEscola, name='CadastroEscola')
]

#Valores
urlpatterns += [
    path('valores/', views.listaValores.as_view(), name='ListaValores'),
    path('valores/cadastrarvalores', views.cadastroValores, name='CadastroValores')
]

#Financeiro
urlpatterns += [
    path('financeiro/', views.listaFinanceiro.as_view(), name='ListaFinanceiro'),
    path('financeiro/cadastrarfinanceiro', views.cadastroFinanceiro, name='CadastroFinanceiro'),
    path('financeiro/<int:pk>', views.detalhesFinanceiro, name='DetalhesFinanceiro'),
    path('financeiro/editar/<int:pk>', views.editarFinanceiro, name='EditarFinanceiro'),
    path('financeiro/deletar/<int:pk>', views.excluirFinanceiro, name='ExcluirFinanceiro')
]

#Chamada
urlpatterns += [
    path('chamada/', views.listaChamada.as_view(), name='ListaChamada'),
    path('chamada/cadastrarchamada', views.cadastroChamada, name='CadastroChamada'),
    path('chamada/<int:pk>', views.detalhesChamada, name='DetalhesChamada'),
    path('chamada/editar/<int:pk>', views.editarChamada, name='EditarChamada'),
    path('chamada/deletar/<int:pk>', views.excluirChamada, name='ExcluirChamada')
]

#Ficha
urlpatterns += [
    path('ficha/', views.listaFicha.as_view(), name='ListaFicha'),
    path('ficha/cadastrarficha', views.cadastroFicha, name='CadastroFicha'),
    path('ficha/<int:pk>', views.detalhesFicha, name='DetalhesFicha'),
    path('ficha/editar/<int:pk>', views.editarFicha, name='EditarFicha'),
    path('ficha/deletar/<int:pk>', views.excluirFicha, name='ExcluirFicha')
]