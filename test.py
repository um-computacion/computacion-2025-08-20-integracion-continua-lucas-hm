import unittest

from main import suma

class TestPrueba(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(5, 8), 13)

if __name__ == "__main__":
    unittest.main()
