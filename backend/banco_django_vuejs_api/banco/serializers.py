from rest_framework import serializers
from .models import Banco, Agencia, Cliente, Conta


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id', 'codigo_banco', 'nome']


class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = ['id', 'nome', 'banco', 'codigo_agencia']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf_cnpj']


class ContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conta
        fields = ['id', 'numero', 'tipo', 'cliente', 'saldo', 'agencia']


class ContaDepositoSerializer(serializers.Serializer):
    valor = serializers.DecimalField(max_digits=19, decimal_places=2, required=True, min_value=0.01)


class ContaSaqueSerializer(serializers.Serializer):
    valor = serializers.DecimalField(max_digits=19, decimal_places=2, required=True, min_value=0.01)
