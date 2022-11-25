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
    path('editaraluno/', views.editarAluno, name='EditarAluno')
]

#Responsavel
urlpatterns += [
    path('listarresponsavel/', views.listaResponsavel.as_view(), name='ListaResponsavel'),
    path('responsavel/cadastrarresponsavel/', views.cadastroResponsavel, name='CadastroResponsavel')
]

#Professor
urlpatterns += [
    path('listarprofessor/', views.listaProfessor.as_view(), name='ListaProfessor'),
    path('professor/cadastrarprofessor', views.cadastroProfessor, name='CadastroProfessor')
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