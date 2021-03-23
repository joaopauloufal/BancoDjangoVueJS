from django.db import models


class Banco(models.Model):
    codigo_banco = models.CharField(verbose_name='Código do Banco', max_length=20, unique=True)
    nome = models.CharField(verbose_name='Nome', max_length=120)

    class Meta:
        ordering = ['codigo_banco']
        verbose_name = 'Banco'

    def __str__(self):
        return f'{self.codigo_banco} - {self.nome}'


class Agencia(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=120)
    banco = models.ForeignKey(Banco, verbose_name='Banco', on_delete=models.PROTECT, related_name='agencias')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Agência'

    def __str__(self):
        return f'{self.id} - {self.nome}'


class Cliente(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=120)
    cpf_cnpj = models.CharField(verbose_name='CPF/CNPJ', max_length=18, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'

    def __str__(self):
        return f'{self.cpf_cnpj} - {self.nome}'


class Conta(models.Model):

    TIPOS_CONTA = (
      ('FISICA', 'Pessoa física'),
      ('JURIDICA', 'Pessoa jurídica'),
    )

    numero = models.CharField(verbose_name='Número', max_length=80)
    saldo = models.DecimalField(verbose_name='Saldo', decimal_places=2, default=0.00, max_digits=19)
    agencia = models.ForeignKey(Agencia, verbose_name='Agência', on_delete=models.PROTECT, related_name='contas')
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT, related_name='contas')
    tipo = models.CharField(verbose_name='Tipo', max_length=15, choices=TIPOS_CONTA)

    class Meta:
        ordering = ['numero']
        verbose_name = 'Conta'
        unique_together = [['cliente', 'tipo', 'agencia']]

    def __str__(self):
        return f'{self.numero} - {self.agencia}: {self.cliente.nome} ({self.tipo})'
