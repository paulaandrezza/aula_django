from django.contrib import admin

from .models import Cargos, Pessoa

admin.site.register(Pessoa)
admin.site.register(Cargos)
