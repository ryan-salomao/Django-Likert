from django.shortcuts import render
from app.forms import FuncionarioForm

def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'form.html', data)