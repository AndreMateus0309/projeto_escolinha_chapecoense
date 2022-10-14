from django.urls import path
from core import views

#Generic
urlpatterns = [
    path('home/', views.index, name='home')
]

#Aluno
urlpatterns += [
    path('listaralunos/', views.listaAlunos.as_view(), name='ListaAlunos'),
    path('alunos/cadastraraluno', views.cadastroAluno, name='CadastroAlunos'),
    path('aluno/verdetalhesaluno/<int:pk>', views.detalhesAluno.as_view(), name='DetalhesAluno'),
    path('aluno/editaraluno/<int:pk>', views.editarAluno, name='EditarAluno'),
    path('aluno/deletaraluno/<int:pk>', views.excluirAluno, name='ExcluirAluno')
]

#Responsavel
urlpatterns += [
    path('listarresponsavel/', views.listaResponsavel.as_view(), name='ListaResponsavel'),
    path('responsavel/cadastrarresponsavel', views.cadastroResponsavel, name='CadastroResponsavel'),
    path('aluno/verdetalhesresponsavel<int:pk>', views.detalhesResponsavel.as_view(), name='DetalhesResponsavel'),
    path('aluno/editarresponsavel/<int:pk>', views.editarResponsavel, name='EditarResponsavel'),
    path('aluno/deletarresponsavel/<int:pk>', views.excluirResponsavel, name='ExcluirResponsavel')
]

#Professor
urlpatterns += [
    path('listarprofessor/', views.listaProfessor.as_view(), name='ListaProfessor'),
    path('professor/cadastrarprofessor', views.cadastroProfessor, name='CadastroProfessor'),
    path('professor/verdetalhesprofessor<int:pk>', views.detalhesProfessor.as_view(), name='DetalhesProfessor'),
    path('professor/editarprofessor/<int:pk>', views.editarProfessor, name='EditarProfessor'),
    path('professor/deletarprofessor/<int:pk>', views.excluirProfessor, name='ExcluirProfessor')
]

#Empresa
urlpatterns += [
    path('listaempresa/', views.listaEmpresa.as_view(), name='ListaEmpresa'),
    path('empresa/cadastrarempresa', views.cadastroEmpresa, name='CadastroEmpresa')
]

#Escola
urlpatterns += [
    path('listaescola/', views.listaEscola.as_view(), name='ListaEscola'),
    path('escola/cadastrarescola', views.cadastroEscola, name='CadastroEscola')
]

#Valores
urlpatterns += [
    path('listavalores/', views.listaValores.as_view(), name='ListaValores'),
    path('valores/cadastrarvalores', views.cadastroValores, name='CadastroValores')
]

#Financeiro
urlpatterns += [
    path('listafinanceiro/', views.listaFinanceiro.as_view(), name='ListaFinanceiro'),
    path('financeiro/cadastrarfinanceiro', views.cadastroFinanceiro, name='CadastroFinanceiro'),
    path('financeiro/detalhesfinanceiro/<int:pk>', views.detalhesFinanceiro, name='DetalhesFinanceiro'),
    path('financeiro/editarfinanceiro/<int:pk>', views.editarFinanceiro, name='EditarFinanceiro'),
    path('financeiro/deletarfinanceiro/<int:pk>', views.excluirFinanceiro, name='ExcluirFinanceiro')
]

#Chamada
urlpatterns += [
    path('listachamada/', views.listaChamada.as_view(), name='ListaChamada'),
    path('chamada/cadastrarchamada', views.cadastroChamada, name='CadastroChamada'),
    path('chamada/detalheschamada/<int:pk>', views.detalhesChamada.as_view(), name='DetalhesChamada'),
    path('chamada/editarchamada/<int:pk>', views.editarChamada, name='EditarChamada'),
    path('chamada/deletarchamada/<int:pk>', views.excluirChamada, name='ExcluirChamada')
]

#Ficha
urlpatterns += [
    path('listaficha/', views.listaFicha.as_view(), name='ListaFicha'),
    path('ficha/cadastrarficha', views.cadastroFicha, name='CadastroFicha'),
    path('ficha/detalhesficha/<int:pk>', views.detalhesFicha.as_view(), name='DetalhesFicha'),
    path('ficha/editarficha/<int:pk>', views.editarFicha, name='EditarFicha'),
    path('ficha/deletarficha/<int:pk>', views.excluirFicha, name='ExcluirFicha')
]