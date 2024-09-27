from django.test import TestCase
from .models import Guitarra
from .serializers import GuitarraSerializer

class GuitarraSerializerTest(TestCase):
    def setUp(self):
        self.guitarra = Guitarra.objects.create(marca="Ibanez", modelo="RG", preco=2999.99, estoque=5)

    def test_guitarra_serializer(self):
        serializer = GuitarraSerializer(self.guitarra)
        self.assertEqual(serializer.data['marca'], 'Ibanez')
        self.assertEqual(serializer.data['modelo'], 'RG')
