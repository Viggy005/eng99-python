from simple_calc import Simplecalc
import unittest

class SimpleCalcTests(unittest.TestCase):
    def test_add(self):
        calc = Simplecalc()
        acutual = calc.add(2,4)
        expected = 6
        self.assertEqual(acutual,expected)