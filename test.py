import unittest

from main import suma
from main import resta

class TestPrueba(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(5, 8), 13)
    def test_resta(self):
	self.assertEqual(resta(5, 2), 3)

if __name__ == "__main__":
    unittest.main()
