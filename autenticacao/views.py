from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
    pessoa = {
        'nome': "Paula Marinho",
        'idade': "23",
        'profissao': "Programadora",
    }

    return render(request, 'cadastro/index.html', {'pessoa': pessoa})
