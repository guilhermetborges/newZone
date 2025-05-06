from django.test import TestCase , Client
from django.urls import reverse_lazy

class indexviewtest(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Teste',
            'email': 'F4K3Q@example.com',
            'assunto': 'Teste',
            'mensagem': 'Teste'
        }
        self.client = Client()

    def test_form_valid(self):
        response = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(response.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Teste',
            'email': 'F4K3Q@example.com',
            'assunto': 'Teste',
        }
        rest = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(rest.status_code, 200)

    
    