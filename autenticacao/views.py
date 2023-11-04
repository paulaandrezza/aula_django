from django.http import HttpResponse
from django.shortcuts import render


def auth(request):
  return HttpResponse("Você está na autenticação")

def cadastro(request):
  return HttpResponse('Faça seu cadastro')