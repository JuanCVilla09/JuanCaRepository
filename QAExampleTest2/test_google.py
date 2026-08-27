import unittest
from main import google_search

class TestGoogleSearch(unittest.TestCase):
    # Test para verificar que la búsqueda de google son correctas
    def test_valid_query(self):
        # Prueba con una consulta válida
        self.assertEqual(google_search("python"), ["python.org", "tutorial python", "aprende python"])

    def test_invalid_query(self):
        # Prueba con una consulta que no tiene resultados
        self.assertEqual(google_search("hola"), ["hola"])

if __name__ == '__main__':
    unittest.main()