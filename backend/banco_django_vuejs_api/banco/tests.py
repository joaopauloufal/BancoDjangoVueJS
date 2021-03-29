from django.test import TestCase
from .factories import AgenciaFactory, BancoFactory, ContaFactory, ClienteFactory
from rest_framework import status
from .models import Banco, Agencia, Cliente, Conta
from django.forms.models import model_to_dict
import factory
import json


class ApiBancoTest(TestCase):

    def test_list(self):
        bancos = BancoFactory.create_batch(3)
        response = self.client.get('/api/v1/bancos/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(bancos), len(response.data))

    def test_list_banco_agencias(self):
        banco = BancoFactory()
        agencias = AgenciaFactory.create_batch(3, banco=banco)
        response = self.client.get(f'/api/v1/bancos/{banco.id}/agencias/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(agencias), len(response.data))

    def test_create(self):
        data = factory.build(dict, FACTORY_CLASS=BancoFactory)
        response = self.client.post('/api/v1/bancos/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Banco.objects.count(), 1)

    def test_create_error(self):
        data = factory.build(dict, FACTORY_CLASS=BancoFactory)
        del data['nome']
        response = self.client.post('/api/v1/bancos/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        banco = BancoFactory()
        response = self.client.get(f'/api/v1/bancos/{banco.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        banco = BancoFactory()
        data = factory.build(dict, FACTORY_CLASS=BancoFactory)
        response = self.client.put(f'/api/v1/bancos/{banco.id}/', data, content_type='application/json')
        banco_atualizado = Banco.objects.first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), model_to_dict(banco_atualizado))

    def test_update_error(self):
        banco = BancoFactory()
        data = factory.build(dict, FACTORY_CLASS=BancoFactory)
        del data['nome']
        response = self.client.put(f'/api/v1/bancos/{banco.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        banco = BancoFactory()
        response = self.client.get(f'/api/v1/bancos/{banco.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/bancos/{banco.id}/')
        response = self.client.get(f'/api/v1/bancos/{banco.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ApiAgenciaTest(TestCase):

    def test_list(self):
        banco = BancoFactory()
        agencias = AgenciaFactory.create_batch(3, banco=banco)
        response = self.client.get('/api/v1/agencias/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(agencias), len(response.data))

    def test_list_agencia_contas(self):
        banco = BancoFactory()
        agencia = AgenciaFactory(banco=banco)
        cliente = ClienteFactory()
        ContaFactory(cliente=cliente, agencia=agencia, tipo='FISICA')
        ContaFactory(cliente=cliente, agencia=agencia, tipo='JURIDICA')
        response = self.client.get(f'/api/v1/agencias/{agencia.id}/contas/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, len(response.data))

    def test_create(self):
        banco = BancoFactory()
        data = factory.build(dict, FACTORY_CLASS=AgenciaFactory, banco=banco)
        data['banco'] = banco.id
        response = self.client.post('/api/v1/agencias/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Banco.objects.count(), 1)

    def test_create_error(self):
        banco = BancoFactory()
        data = factory.build(dict, FACTORY_CLASS=AgenciaFactory, banco=banco, content_type='application/json')
        del data['nome']
        response = self.client.post('/api/v1/agencias/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        banco = BancoFactory()
        agencia = AgenciaFactory(banco=banco)
        response = self.client.get(f'/api/v1/agencias/{agencia.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        banco = BancoFactory()
        agencia = AgenciaFactory(banco=banco)
        data = factory.build(dict, FACTORY_CLASS=AgenciaFactory)
        data['banco'] = banco.id
        response = self.client.put(f'/api/v1/agencias/{agencia.id}/', data, content_type='application/json')
        agencia_atualizada = Agencia.objects.first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), model_to_dict(agencia_atualizada))

    def test_update_error(self):
        banco = BancoFactory()
        agencia = AgenciaFactory(banco=banco)
        data = factory.build(dict, FACTORY_CLASS=AgenciaFactory, banco=banco)
        data['banco'] = banco.id
        del data['nome']
        response = self.client.put(f'/api/v1/agencias/{agencia.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        banco = BancoFactory()
        agencia = AgenciaFactory(banco=banco)
        response = self.client.get(f'/api/v1/agencias/{agencia.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/agencias/{agencia.id}/')
        response = self.client.get(f'/api/v1/agencias/{agencia.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ApiClienteTest(TestCase):

    def test_list(self):
        clientes = ClienteFactory.create_batch(3)
        response = self.client.get('/api/v1/clientes/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(clientes), len(response.data))

    def test_create(self):
        data = factory.build(dict, FACTORY_CLASS=ClienteFactory)
        response = self.client.post('/api/v1/clientes/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)

    def test_list_cliente_contas(self):
        banco = BancoFactory()
        agencia = AgenciaFactory(banco=banco)
        cliente = ClienteFactory()
        ContaFactory(cliente=cliente, agencia=agencia, tipo='FISICA')
        ContaFactory(cliente=cliente, agencia=agencia, tipo='JURIDICA')
        response = self.client.get(f'/api/v1/clientes/{cliente.id}/contas/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, len(response.data))

    def test_create_error(self):
        data = factory.build(dict, FACTORY_CLASS=ClienteFactory)
        del data['nome']
        response = self.client.post('/api/v1/clientes/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        cliente = ClienteFactory()
        response = self.client.get(f'/api/v1/clientes/{cliente.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        cliente = ClienteFactory()
        data = factory.build(dict, FACTORY_CLASS=ClienteFactory)
        response = self.client.put(f'/api/v1/clientes/{cliente.id}/', data, content_type='application/json')
        cliente_atualizado = Cliente.objects.first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), model_to_dict(cliente_atualizado))

    def test_update_error(self):
        cliente = ClienteFactory()
        data = factory.build(dict, FACTORY_CLASS=ClienteFactory)
        del data['nome']
        response = self.client.put(f'/api/v1/clientes/{cliente.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        cliente = ClienteFactory()
        response = self.client.get(f'/api/v1/clientes/{cliente.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/clientes/{cliente.id}/')
        response = self.client.get(f'/api/v1/clientes/{cliente.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ApiContaTest(TestCase):

    def setUp(self):
        self.banco = BancoFactory()
        self.agencia = AgenciaFactory(banco=self.banco)
        self.cliente = ClienteFactory()

    def test_list(self):
        contas = ContaFactory.create_batch(3)
        response = self.client.get('/api/v1/contas/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(contas), len(response.data))

    def test_create(self):
        data = factory.build(dict, FACTORY_CLASS=ContaFactory, cliente=self.cliente, agencia=self.agencia)
        data['cliente'] = self.cliente.id
        data['agencia'] = self.agencia.id
        response = self.client.post('/api/v1/contas/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conta.objects.count(), 1)

    def test_create_error(self):
        data = factory.build(dict, FACTORY_CLASS=ContaFactory, cliente=self.cliente, agencia=self.agencia)
        data['cliente'] = self.cliente.id
        data['agencia'] = self.agencia.id
        del data['agencia']
        response = self.client.post('/api/v1/contas/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        conta = ContaFactory()
        response = self.client.get(f'/api/v1/contas/{conta.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        conta = ContaFactory()
        data = factory.build(dict, FACTORY_CLASS=ContaFactory, cliente=self.cliente, agencia=self.agencia)
        data['cliente'] = self.cliente.id
        data['agencia'] = self.agencia.id
        response = self.client.put(f'/api/v1/contas/{conta.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_error(self):
        conta = ContaFactory()
        data = factory.build(dict, FACTORY_CLASS=ContaFactory, cliente=self.cliente, agencia=self.agencia)
        data['cliente'] = self.cliente.id
        del data['agencia']
        response = self.client.put(f'/api/v1/contas/{conta.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        conta = ContaFactory()
        response = self.client.get(f'/api/v1/contas/{conta.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/contas/{conta.id}/')
        response = self.client.get(f'/api/v1/contas/{conta.id}/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_insert_contas_mesmo_tipo_agencia_error(self):
        data = factory.build(dict, FACTORY_CLASS=ContaFactory, cliente=self.cliente, agencia=self.agencia, tipo='FISICA')
        data['cliente'] = self.cliente.id
        data['agencia'] = self.agencia.id
        response = self.client.post('/api/v1/contas/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/api/v1/contas/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_saque_success(self):
        conta = ContaFactory(cliente=self.cliente, agencia=self.agencia, saldo=80.00)
        data = {
            'valor': 50.00
        }
        response = self.client.put(f'/api/v1/contas/{conta.id}/sacar/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        message = {'message': 'Saque realizado com sucesso!'}
        self.assertEqual(message, response.data)

        conta = Conta.objects.first()
        self.assertEqual(conta.saldo, 30.00)

    def test_saque_valor_menor_que_saldo(self):
        conta = ContaFactory(cliente=self.cliente, agencia=self.agencia, saldo=80.00)
        data = {
            'valor': 90.00
        }
        response = self.client.put(f'/api/v1/contas/{conta.id}/sacar/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        message = 'Saldo insuficiente.'
        self.assertEqual(message, response.data['valor'][0])

    def test_saque_valor_negativo(self):
        conta = ContaFactory(cliente=self.cliente, agencia=self.agencia, saldo=80.00)
        data = {
            'valor': -5.00
        }
        response = self.client.put(f'/api/v1/contas/{conta.id}/sacar/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_saque_valor_zerado(self):
        conta = ContaFactory(cliente=self.cliente, agencia=self.agencia, saldo=80.00)
        data = {
            'valor': 0.00
        }
        response = self.client.put(f'/api/v1/contas/{conta.id}/sacar/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deposito_success(self):
        conta = ContaFactory(cliente=self.cliente, agencia=self.agencia, saldo=80.00)
        data = {
            'valor': 50.00
        }
        response = self.client.put(f'/api/v1/contas/{conta.id}/depositar/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        message = {'message': 'Depósito realizado com sucesso!'}
        self.assertEqual(message, response.data)

        conta = Conta.objects.first()
        self.assertEqual(conta.saldo, 130.00)

    def test_deposito_valor_negativo(self):
        conta = ContaFactory(cliente=self.cliente, agencia=self.agencia, saldo=80.00)
        data = {
            'valor': -5.00
        }
        response = self.client.put(f'/api/v1/contas/{conta.id}/depositar/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deposito_valor_zerado(self):
        conta = ContaFactory(cliente=self.cliente, agencia=self.agencia, saldo=80.00)
        data = {
            'valor': 0.00
        }
        response = self.client.put(f'/api/v1/contas/{conta.id}/depositar/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
