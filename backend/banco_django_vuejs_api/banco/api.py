from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Banco, Agencia, Cliente, Conta
from .serializers import BancoSerializer, AgenciaSerializer, ClienteSerializer, ContaSerializer


class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer

    @action(detail=True, methods=['get'], serializer_class=AgenciaSerializer)
    def agencias(self, request, *args, **kwargs):
        banco = self.get_object()
        agencias = self.get_serializer(banco.agencias, many=True)
        return Response(agencias.data)


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

    @action(detail=True, methods=['get'], serializer_class=ContaSerializer)
    def contas(self, request, *args, **kwargs):
        agencia = self.get_object()
        contas = self.get_serializer(agencia.contas, many=True)
        return Response(contas.data)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=True, methods=['get'], serializer_class=ContaSerializer)
    def contas(self, request, *args, **kwargs):
        cliente = self.get_object()
        contas = self.get_serializer(cliente.contas, many=True)
        return Response(contas.data)


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
