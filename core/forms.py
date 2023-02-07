from django import forms
from .models import *

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = "__all__"

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = "__all__"

class ValoresForm(forms.ModelForm):
    class Meta:
        model = Valores
        fields = "__all__"

class FinanceiroForm(forms.ModelForm):
    class Meta:
        model = Financeiro
        fields = "__all__"

class ChamadaForm(forms.ModelForm):
    class Meta:
        model = Chamada
        fields = "__all__"

class FinanceiroForm(forms.ModelForm):
    class Meta:
        model = Financeiro
        fields = "__all__"

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = "__all__"
