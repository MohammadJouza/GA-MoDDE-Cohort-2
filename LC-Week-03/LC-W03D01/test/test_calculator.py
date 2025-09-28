# test/test_calculator.py
import unittest
from nose2.tools import params

# need to import the Calculator class from ile
from src import calculator

# from src.calculator import Calculator


class TddInPythonExample(unittest.TestCase):

    # method (execute each )
    def setUp(self):
        self.calc = calculator.Calculator()

    # { calc:class()   }

    def test_calculator_add_method_returns_correct_result(self):
        # calc = calculator.Calculator()
        # calc = Calculator()
        result_1 = self.calc.add(4, 4)
        # func(), result we are expected
        # actual first, expected second
        self.assertEqual(result_1, 8)

    def test_1(self):
        result_1 = self.calc.add(2, 4)
        self.assertEqual(result_1, 6)

    def test_2(self):
        result_1 = self.calc.add(20, 2)
        self.assertEqual(result_1, 22)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        #                 error, method, par ....
        self.assertRaises(ValueError, self.calc.add, "two", "three")

    def test_3(self):
        self.assertRaises(ValueError, self.calc.add, 4, "three")

    def test_4(self):
        self.assertRaises(ValueError, self.calc.add, "two", 5)
        # YS: test pass (code cover this case),
        # NO: Error (in the testing),
        # <<: test wil not pass (code not cover this case)

    # example of powerful in nose2
    @params((1, 1, 2), (2.0, 1.5, 3.5), (4, 5, 9))
    def test_multi(self, x, y, expected):
        print("x: ", x)
        print("y: ", y)
        result_1 = self.calc.add(x, y)
        self.assertEqual(result_1, expected)

    # !- HW: True / False
    # 1.1- check True / False
    # 1.2- read about isinstance with bool
    # 1.3- read about how to get all the parents and grand class
    # 1.4- what we can do to check only the one we need `accepted_classes` check src/calculator.py

    # !- HW 2- Practicing Problem Solving

    # !- Extra HW CI/CD 


"""  
standard unittest runner
if __name__ == '__main__':
    unittest.main()

"""
