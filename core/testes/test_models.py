from model_mommy import mommy
from django.test import TestCase
from core.models import get_file_path, Servico, Contato
import uuid

class GetFilePathTest(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        result = get_file_path(None , 'servico.png')
        self.assertEqual(len(result), len(self.filename))

class ServicoModelTest(TestCase):
    def setUp(self):
        self.servico = mommy.make(Servico)

    def test_str(self):
        expected = self.servico.servico
        result = Servico.__str__(self.servico)  # ou apenas str(self.servico)
        self.assertEqual(expected, result)


class ContatoModelTest(TestCase):
    def setUp(self):
        self.contato = mommy.make(Contato)

    def test_str(self):
        expected = self.contato.nome
        result = Contato.__str__(self.contato)
        self.assertEqual(expected, result)