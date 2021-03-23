from rest_framework import serializers
from .models import Banco, Agencia, Cliente


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id', 'codigo_banco', 'nome']


class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = ['id', 'nome', 'banco']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf_cnpj']
