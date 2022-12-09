from django.urls import path
from core import views

#Generic
urlpatterns = [
    path('home/', views.index, name='home')
]

#Aluno
urlpatterns += [
    path('listaralunos/', views.listaAlunos.as_view(), name='ListaAlunos'),
    path('cadastraraluno/', views.cadastroAluno, name='CadastroAlunos'),
    path('editaraluno/<int:pk>', views.editarAluno, name='EditarAluno'),
    path('excluiraluno/<int:pk>', views.excluirAluno, name='ExcluirAluno'),
    path('detalhesaluno/<int:pk>', views.detalhesAluno.as_view(), name='DetalhesAluno')
]

#Responsavel
urlpatterns += [
    path('listarresponsavel/', views.listaResponsavel.as_view(), name='ListaResponsavel'),
    path('responsavel/cadastrarresponsavel/', views.cadastroResponsavel, name='CadastroResponsavel'),
    path('editarresponsavel/', views.editarResponsavel, name='EditarResponsavel'),
    path('excluirresponsavel/', views.excluirResponsavel, name='ExcluirResponsavel')

]

#Professor
urlpatterns += [
    path('listarprofessor/', views.listaProfessor.as_view(), name='ListaProfessor'),
    path('professor/cadastrarprofessor', views.cadastroProfessor, name='CadastroProfessor'),
    path('editarprofessor/', views.editarProfessor, name='EditarProfessor'),
    path('excluirprofessor/', views.excluirProfessor, name='ExcluirProfessor')
]

#Empresa
urlpatterns += [
    path('listaempresa/', views.listaEmpresa.as_view(), name='ListaEmpresa'),
    path('empresa/cadastrarempresa', views.cadastroEmpresa, name='CadastroEmpresa'),
    path('editaraluno/', views.editarAluno, name='EditarAluno'),
    path('excluiraluno/', views.excluirAluno, name='ExcluirAluno')
]

#Escola
urlpatterns += [
    path('listaescola/', views.listaEscola.as_view(), name='ListaEscola'),
    path('escola/cadastrarescola', views.cadastroEscola, name='CadastroEscola'),
    path('editarescola/', views.editarEscola, name='EditarEscola'),
    path('excluirescola/', views.excluirEscola, name='ExcluirEscola')
]

#Valores
urlpatterns += [
    path('listavalores/', views.listaValores.as_view(), name='ListaValores'),
    path('valores/cadastrarvalores', views.cadastroValores, name='CadastroValores'),
    path('editarvalores/', views.editarValores, name='EditarValores'),
    path('excluirvalores/', views.excluirValores, name='ExcluirValores')
]

#Financeiro
urlpatterns += [
    path('listafinanceiro/', views.listaFinanceiro.as_view(), name='ListaFinanceiro'),
    path('financeiro/cadastrarfinanceiro', views.cadastroFinanceiro, name='CadastroFinanceiro')
]

#Chamada
urlpatterns += [
    path('listachamada/', views.listaChamada.as_view(), name='ListaChamada'),
    path('chamada/cadastrarchamada', views.cadastroChamada, name='CadastroChamada')
]

#Ficha
urlpatterns += [
    path('listaficha/', views.listaFicha.as_view(), name='ListaFicha'),
    path('ficha/cadastrarficha', views.cadastroFicha, name='CadastroFicha')
]