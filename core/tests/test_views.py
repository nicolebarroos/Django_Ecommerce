from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth import get_user_model
from django.conf import settings

from model_bakery import baker

User = get_user_model()
#Iniciando o teste para o index
class IndexViewTestCase(TestCase): #TestCase, tipo de teste django baseados em classe
    #dentro do TestCase, chamamos o Client
    #Client atua como um cliente testando requisições, como GET, POST, urls, requerimentos... 
    def setUp(self): 
        self.client = client()
        self.url = reverse('index') #testando url reverse

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200) #testando o status 200(sucess)
    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html') #testando a usuabilidade do template
