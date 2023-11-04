from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
  return render(request, 'cadastro/index.html')