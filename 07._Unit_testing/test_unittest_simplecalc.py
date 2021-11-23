from simple_calc import SimpleCalc
import unittest

class SimpleCalcTests(unittest.TestCase):
    def setUp(self):# runs first before all others tests
        self.calc = SimpleCalc()

    #def tearDown(self):# runs at end of all tests

    def test_add(self):
        #calc = SimpleCalc()
        actual = self.calc.add(2,4)
        expected = 6
        self.assertEqual(actual,expected) # very important

    def test_sub(self):
        #calc = SimpleCalc()
        actual = self.calc.sub(4,2)
        expected = 2
        self.assertEqual(actual,expected)

    def test_mul(self):
        calc = SimpleCalc()
        actual = calc.mul(2,4)
        expected = 8
        self.assertEqual(actual,expected)

    def test_div(self):
        calc = SimpleCalc()
        actual = calc.div(5,2)
        expected = 2.5
        self.assertEqual(expected,actual,"Expected divide")





