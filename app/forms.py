from django.forms import ModelForm
from app.models import Funcionario

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['atendimento', 'pontualidade', 'qualidade']