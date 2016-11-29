import unittest
from CalCalc import calculate

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate('1+2'),'3')

    def test_subtract(self):
        self.assertEqual(calculate('0-1'),'-1')

    def test_div_by_zero(self):
        self.assertEqual(calculate('1/0'),'infinity^~')

    def test_multiply(self):
        self.assertEqual(calculate('10*10'),'100')

    def test_silly(self):
        self.assertEqual(calculate('diameter of earth in lightyears'),
                         '1.3468323×10^-9 ly  (light years)')
        
    def test_question(self):
        self.assertEqual(calculate('mass of moon in kg'),'7.3459×10^22 kg  (kilograms)')


if __name__ == '__main__':
        unittest.main()
