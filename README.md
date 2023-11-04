# aula_django

## Configurações iniciais

Primeiro vamos criar e ativar o ambiente virtual:

```bash
+# Criar
	# Linux
		python3 -m venv venv
	# Windows
		python -m venv venv

#Ativar
	# Linux
		source venv/bin/activate
	# Windows
		source venv/Scripts/Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

	Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Instale as bibliotecas:

```bash
pip install django
pip install pillow
```

Inicio um projeto Django

```bash
django-admin startproject <nome_do_projeto> .
```

Para criar um app:

```bash
python3 manage.py startapp <nome_do_app>
```

Dentro de `<nome_do_projeto>/urls.py` ficam as rotas para os apps, é importante criar uma rota para o novo app que acabamos de criar

```python
from django.urls import include

path('<rota>/', include('<nome_do_app>.urls')),
```

É preciso criar dentro da pasta `<nome_do_app>` o arquivo `urls.py` onde serão configurados as outras rotas da mesma forma que foi configurado em `<nome_do_projeto>/urls.py`, mas dessa vez a rota irá apontar para as views, que serão a renderização da página na rota especificada, por exemplo:

```python
from django.urls import include
from . import views

path('cadastro/', views.cadastro),
```

A rota `cadastro\` aponta pra função cadastro dentro de views, que pode ser criada da seguinte forma dentro do arquivo `views.py` que está dentro da mesma pasta do app, onde cadastro.html é o arquivo que será renderizado:

```python
from django.shortcuts import render

def cadastro(request):
    return render(request, 'cadastro.html')
```
