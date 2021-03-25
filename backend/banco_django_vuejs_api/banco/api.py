from rest_framework import viewsets, response, status, serializers, filters
from rest_framework.decorators import action
from .models import Banco, Agencia, Cliente, Conta
from .serializers import (
    BancoSerializer, AgenciaSerializer, ClienteSerializer, ContaSerializer, ContaDepositoSerializer,
    ContaSaqueSerializer
)
from decimal import Decimal
from django.db.transaction import atomic


class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['codigo_banco', 'nome']

    @action(detail=True, methods=['get'], serializer_class=AgenciaSerializer)
    def agencias(self, request, *args, **kwargs):
        banco = self.get_object()
        agencias = self.get_serializer(banco.agencias, many=True)
        return response.Response(agencias.data)


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'codigo_agencia']

    @action(detail=True, methods=['get'], serializer_class=ContaSerializer)
    def contas(self, request, *args, **kwargs):
        agencia = self.get_object()
        contas = self.get_serializer(agencia.contas, many=True)
        return response.Response(contas.data)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cpf_cnpj']

    @action(detail=True, methods=['get'], serializer_class=ContaSerializer)
    def contas(self, request, *args, **kwargs):
        cliente = self.get_object()
        contas = self.get_serializer(cliente.contas, many=True)
        return response.Response(contas.data)


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['numero', 'cliente__cpf_cnpj']

    @atomic
    @action(detail=True, methods=['put'], serializer_class=ContaDepositoSerializer)
    def depositar(self, request, *args, **kwargs):
        conta = self.get_object()
        serializer = ContaDepositoSerializer(data=request.data)
        if serializer.is_valid():
            conta.saldo += Decimal(serializer.data['valor'])
            conta.save()
            return response.Response({'message': 'Depósito realizado com sucesso!'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @atomic
    @action(detail=True, methods=['put'], serializer_class=ContaSaqueSerializer)
    def sacar(self, request, *args, **kwargs):
        conta = self.get_object()
        serializer = ContaDepositoSerializer(data=request.data)
        if serializer.is_valid():
            valor = Decimal(serializer.data['valor'])
            if valor > conta.saldo:
                raise serializers.ValidationError({'valor': ['Saldo insuficiente.']})
            conta.saldo -= valor
            conta.save()
            return response.Response({'message': 'Saque realizado com sucesso!'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
