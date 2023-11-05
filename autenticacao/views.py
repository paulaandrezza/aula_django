import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Cargos, Pessoa


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/index.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        cargo = Cargos.objects.get(id=2)

        pessoa = Pessoa(nome=nome, email=email, senha=senha, cargo=cargo)
        pessoa.save()
        return HttpResponse('Cadastro realizado com sucesso')


def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar/index.html', {'pessoas': pessoas})
