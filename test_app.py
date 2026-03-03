import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Crée un client de test pour l'application Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        # Fait une requête GET sur "/"
        response = self.app.get('/')
        # Vérifie le code HTTP
        self.assertEqual(response.status_code, 200)
        # Vérifie le contenu de la réponse
        self.assertEqual(response.data.decode(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
