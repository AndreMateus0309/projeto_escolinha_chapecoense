from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"
        widgets = {
            'dataNascimento': DateInput(),
            'cpf': CPFField()
        }

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = "__all__"
        widgets = {
            'dataNascimento': DateInput()
        }

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
        widgets = {
            'dataMovimento': DateInput(),
        }

class ChamadaForm(forms.ModelForm):
    class Meta:
        model = Chamada
        fields = "__all__"
        widgets = {
            'data': DateInput(),
        }

class FinanceiroForm(forms.ModelForm):
    class Meta:
        model = Financeiro
        fields = "__all__"
        widgets = {
            'dataMovimento': DateInput(),
        }

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = "__all__"
        widgets = {
            'data': DateInput(),
        }
