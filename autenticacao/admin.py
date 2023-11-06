from django.contrib import admin

from .models import Cargos, Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    readonly_fields = ('senha',)
    search_fields = ("nome",)
    list_filter = ('cargo',)
    list_editable = ('email',)


admin.site.register(Cargos)
