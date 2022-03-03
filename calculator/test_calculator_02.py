# EXAMPLE OF UNIT-TESTING FOR A SIMPLE CALCULATOR PART 02
# Santiago Garcia Arango

# Own imports
import calculator

# Built-in imports
import unittest


class TestCalculator(unittest.TestCase):
    """
    TestCalculator inherits from unittest.TestCase in order to get special 
    methods that enable testing our Calculator.
    """

    @classmethod
    def setUpClass(cls):
        """
        This is an special method that is executed only once for the whole 
        class, just when the class object is created.
        """
        cls.calc = calculator.Calculator()

    def test_add(self):
        print("\n-->Used calculator object: ", self.calc)
        self.assertEqual(self.calc.add(12, 6), 18)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_subtract(self):
        print("\n-->Used calculator object: ", self.calc)
        self.assertEqual(self.calc.subtract(12, 6), 6)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-10, -5), -5)

    def test_multiply(self):
        print("\n-->Used calculator object: ", self.calc)
        self.assertEqual(self.calc.multiply(12, 6), 72)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        print("\n-->Used calculator object: ", self.calc)
        self.assertEqual(self.calc.divide(12, 6), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
