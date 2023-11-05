# aula_django

## Requisitos

### Extensões

- [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) para visualizar o banco de dados no vs-code
- [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8) para formatar o código automaticamente
- [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) para sintaxe colorida no código django
- [djLint](https://marketplace.visualstudio.com/items?itemName=monosans.djlint) para formatar o código django-html

### JSON config

```json
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.autopep8",
    "editor.tabSize": 4,
    "editor.insertSpaces": true
  },
  "emmet.includeLanguages": { "django-html": "html" },
  "[django-html]": {
    "editor.defaultFormatter": "monosans.djlint"
  },
```

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
# Para lidar com imagens
pip install pillow
```

Inicie um projeto Django

```bash
django-admin startproject <nome_do_projeto> .
```

<br>

### Configurando arquivos estáticos

Dentro de <nome_do_projeto>/settings.py digite:

```python
import os

TEMPLATES = [
    {
        ...
        #Para tornar o diretório raiz dinâmico idepentende do sistema operacional
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]

# Configurações para arquivos estaticos
STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

<br>

### Criando um novo app

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

A rota `cadastro\` aponta pra função cadastro dentro de views, que pode ser criada da seguinte forma dentro do arquivo `views.py` que está dentro da mesma pasta do app, onde `index.html` é o arquivo que será renderizado, é importante que esse arquivo esteja dentro da pasta `templates` que precisa ser criada dentro da pasta do app:

```python
from django.shortcuts import render

def cadastro(request):
    return render(request, 'index.html')
```

Sempre que criar um no app é importante cadastrá-lo dentro do array `INSTALLED_APPS` que está dentro de `<nome_do_projeto>/settings.py`:

```python
INSTALLED_APPS = [
    ... ,
		'<nome_do_app>'
]
```

<br>

### Passando dados na renderização

Para isso basta incluir um dicionario dentro de render dentro de `views.py` como no exemplo:

```python
def cadastro(request):
  nome = "Paula Marinho"
  idade = "23"
  profissao = "Programadora"

  return render(request, 'cadastro/index.html', {
    'nome': nome,
    'idade': idade,
    'profissao': profissao,
  })
```

Para utilizar esses dados, basta referência-los no html dentro de chaves duplas `({{}})` como no exemplo:

```html
<h1>Nome: {{nome}}</h1>
<h1>Idade: {{idade}}</h1>
<h1>Profissao: {{profissao}}</h1>
```

<br>

### Como mostrar imagens dentro do html

Primeiro copie a imagem que deseja para dentro de `templates/static/img`, depois dentro do arquivo html, basta colocar o seguinte código:

```html
<!-- Para carregar a rota static que foi configurada em settings.py -->
{% load static %}

<!-- Renderizar a imagem -->
<img src="{% static 'img/front-back-cat.jpg' %}" />
```

O mesmo vale para arquivos css e js que deseje inserir no html, a referência é feita utilizando o `static`

<br>

### Banco de dados

Nesse projeto iremos utilizar o sqlite3, que é o banco padrão que o projeto inicia, mas caso queira alterar o banco, é só mudar em `settings.py` o dicionario `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Para iniciar o banco de dados com as tabelas do django, no terminal digite:

```bash
python manage.py makemigrations
python manage.py migrate
```

Para criar tabelas no banco de dados, dentro de cada app, no arquivo `models.py` crie tabelas como no exemplo:

```python
from django.db import models
from django.db.models.fields import CharField, EmailField


class Pessoa(models.Model):
    nome = CharField(max_length=100)
    email = EmailField
    senha = CharField(max_length=100)

```

Para salvar as informações no banco de dados é necessário realizar os comandos de `makemigrations` e `migrate` anteriores.

<br>

### Salvando dados no banco de dados

Para isso, basta dentro da função que é chamada quando acontece o envio dos dados instanciar um objeto da classe desejava e após passar os dados salva-lo no banco, como no exemplo abaixo:

```python
from .models import Pessoa
    pessoa = Pessoa(nome=nome, email=email, senha=senha)
    pessoa.save()
```

