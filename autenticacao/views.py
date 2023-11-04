from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
  nome = "Paula Marinho"
  idade = "23"
  profissao = "Programadora"
  
  return render(request, 'cadastro/index.html', {
    'nome': nome,
    'idade': idade,
    'profissao': profissao,
  })