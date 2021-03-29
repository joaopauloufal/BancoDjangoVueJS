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


class ClienteFactory(factory.django.DjangoModelFactory):

    nome = factory.Sequence(lambda n: fake.name())
    cpf_cnpj = factory.Sequence(lambda n: fake.numerify('###.###.###-##'))

    class Meta:
        model = Cliente


class ContaFactory(factory.django.DjangoModelFactory):

    numero = factory.Sequence(lambda n: fake.swift8())
    saldo = factory.Sequence(lambda n: fake.pyfloat(1, 2))

    class Meta:
        model = Conta
        django_get_or_create = ('tipo', )
