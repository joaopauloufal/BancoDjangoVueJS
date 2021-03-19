from django.db import models


class Banco(models.Model):
    codigo_banco = models.CharField(verbose_name='Código do Banco', max_length=20)
    nome = models.CharField(verbose_name='Nome', max_length=120)


class Agencia(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=120)
    banco = models.ForeignKey(Banco, verbose_name='Banco', on_delete=models.PROTECT, related_name='agencias')


class Cliente(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=120)
    cpf_cnpj = models.CharField(verbose_name='CPF/CNPJ', max_length=18)


class Conta(models.Model):

    TIPOS_CONTA = (
      ('FISICA', 'Pessoa física'),
      ('JURIDICA', 'Pessoa jurídica'),
    )

    numero = models.CharField(verbose_name='Número', max_length=80)
    saldo = models.DecimalField(verbose_name='Saldo', decimal_places=2, default=0.00)
    agencia = models.ForeignKey(Agencia, verbose_name='Agência', on_delete=models.PROTECT, related_name='contas')
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT, related_name='contas')
    tipo = models.CharField(verbose_name='Tipo', max_length=15, choices=TIPOS_CONTA)
