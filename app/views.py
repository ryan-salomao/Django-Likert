from django.shortcuts import render, redirect
from app.forms import FuncionarioForm
from app.models import Funcionario

def home(request):
    data = {}
    data['db'] = Funcionario.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'form.html', data)

def create(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')