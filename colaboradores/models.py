from django.db import models
import re
from django.core.exceptions import ValidationError


def valida_cpf(value):
    if not re.match(r'^\d{11}$', value):
        raise ValidationError('O CPF deve conter exatamente 11 dígitos e somente números.')

class Colaboradores(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True, validators=[valida_cpf])
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()

    class Meta:
        db_table = 'colaboradores"."Colaboradores'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome
