# coding=utf-8

from django.test import TestCase, Client
# Teste unitário, Teste de integração ...

class IndexViewTestCase(TestCase):
	def setUp(self):
		self.client = Client()

	def tearDown(self):
		pass

	def test_status_code(self):
		response = self.client.get('/') # acessar a url: http://127.0.0.1:8000/
		self.assertEqual(response.status_code, 200) # Faz um teste pra saber se o status_code é igual a 200

	def test_template_used(self):
		response = self.client.get('/') # acessar a url: http://127.0.0.1:8000/
		self.assertTemplateUsed(response, 'index.html')