from django.db import models
from django.db.models.fields import CharField, EmailField


class Pessoa(models.Model):
    nome = CharField(max_length=100)
    email = EmailField()
    senha = CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
