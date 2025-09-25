from unittest import TestCase
import inspect

from src.add import addition, Calculator



class TestCalculator(TestCase):
    def test_add_positive_number(self):
        calc = Calculator(10, 20)
        self.assertEqual(calc.addition(), 30)

    def test_invalid_input_types(self):
        calc = Calculator("a", "b")

        with self.assertRaises(ValueError):
            calc.addition()
        
        calc = Calculator(0.1, 5.2)

        with self.assertRaises(ValueError):
            calc.addition()
        
        calc = Calculator(True, False)

        with self.assertRaises(ValueError):
            calc.addition()      

    def test_add_negative_number(self):
        calc = Calculator(-10, 20)
        self.assertEqual(calc.addition(), 10)

    
class TestAdd(TestCase):

    def test_add(self):
        # assertion method (expected_value)
        self.assertEqual(addition(5, 6), 11)


class TestClass01(TestCase):
    def test_case02(self):
        print()
        # print("\nRunning Test Method : " + inspect.stack()[0][3])

    def test_case01(self):
        print()
        # print("\nRunning Test Method : " + inspect.stack()[0][3])
