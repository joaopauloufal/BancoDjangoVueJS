from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Banco, Agencia, Cliente
from .serializers import BancoSerializer, AgenciaSerializer, ClienteSerializer


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


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
