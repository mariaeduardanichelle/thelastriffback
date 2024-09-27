from django.test import TestCase

from django.test import TestCase
from .models import Guitarra

class GuitarraModelTest(TestCase):
    def setUp(self):
        Guitarra.objects.create(marca="Fender", modelo="Stratocaster", preco=1999.99, estoque=10)

    def test_guitarra_creation(self):
        guitarra = Guitarra.objects.get(marca="Fender")
        self.assertEqual(guitarra.modelo, "Stratocaster")
        self.assertEqual(str(guitarra), "Fender (Stratocaster)")
