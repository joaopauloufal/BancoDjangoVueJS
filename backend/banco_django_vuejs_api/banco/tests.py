from django.test import TestCase
from .factories import AgenciaFactory, BancoFactory
from rest_framework import status
from .models import Banco
from django.forms.models import model_to_dict
import factory
import json


class ApiBancoTest(TestCase):

    def test_list(self):
        bancos = BancoFactory.create_batch(3)
        response = self.client.get('/api/v1/bancos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(bancos), len(response.data))

    def test_list_banco_agencias(self):
        banco = BancoFactory()
        AgenciaFactory(banco=banco)
        response = self.client.get(f'/api/v1/bancos/{banco.id}/agencias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))

    def test_create(self):
        data = factory.build(dict, FACTORY_CLASS=BancoFactory)
        response = self.client.post('/api/v1/bancos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Banco.objects.count(), 1)

    def test_create_error(self):
        data = factory.build(dict, FACTORY_CLASS=BancoFactory)
        del data['nome']
        response = self.client.post('/api/v1/bancos/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        banco = BancoFactory()
        response = self.client.get(f'/api/v1/bancos/{banco.id}/')
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
        response = self.client.get(f'/api/v1/bancos/{banco.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/bancos/{banco.id}/')
        response = self.client.get(f'/api/v1/bancos/{banco.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
