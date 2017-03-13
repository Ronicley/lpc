from __future__ import unicode_literals
from django.db import models

from django.db import models
from django.utils import timezone

class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    local = models.CharField('local', max_length=200)
    email = models.EmailField('e-mail', max_length=100)
    qtdInscricoes = models.IntegerField(null=True)

    def __repr__(self):
        return self.nome
# Create your models here.
