import factory
from .models import Banco, Agencia, Cliente, Conta
from faker import Faker

fake = Faker()


class BancoFactory(factory.django.DjangoModelFactory):

    nome = factory.Sequence(lambda n: fake.name())
    codigo_banco = factory.Sequence(lambda n: fake.swift8())

    class Meta:
        model = Banco


class AgenciaFactory(factory.django.DjangoModelFactory):

    nome = factory.Sequence(lambda n: fake.name())
    codigo_agencia = factory.Sequence(lambda n: fake.swift8())

    class Meta:
        model = Agencia
        django_get_or_create = ('banco',)


class ClienteFactory(factory.django.DjangoModelFactory):

    nome = fake.name()
    cpf_cnpj = factory.Sequence(lambda: fake.numerify('###.###.###-##'))

    class Meta:
        model = Cliente


class ContaFactory(factory.django.DjangoModelFactory):

    numero = fake.swift8()
    saldo = fake.pyfloat(1, 2)

    class Meta:
        model = Conta
        django_get_or_create = ('agencia', 'cliente', 'tipo', )
