import unittest
from Calculator import Calculator
from CSVReader import read_csv


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition_method(self):
        calculator = Calculator()
        test_cases = read_csv("src/test/Unit Test Addition.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.add(int(test_case[0]), int(test_case[1])), int(test_case[2]))
        print(len(test_cases), " test cases passed for Addition!")

    def test_multiplication_method(self):
        calculator = Calculator()
        test_cases = read_csv("src/test/Unit Test Multiplication.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.multiply(int(test_case[0]), int(test_case[1])), int(test_case[2]))
        print(len(test_cases), " test cases passed for Multiplication!")

    def test_subtraction_method(self):
        calculator = Calculator()
        test_cases = read_csv("src/test/Unit Test Subtraction.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.subtract(int(test_case[1]), int(test_case[0])), int(test_case[2]))
        print(len(test_cases), " test cases passed for Subtraction!")

    def test_squaring_method(self):
        calculator = Calculator()
        test_cases = read_csv("src/test/Unit Test Square.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.square(int(test_case[0])), int(test_case[1]))
        print(len(test_cases), " test cases passed for Squaring!")

    def test_square_root_method(self):
        calculator = Calculator()
        test_cases = read_csv("src/test/Unit Test Square Root.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.sqrt(int(test_case[0])), float(test_case[1]))
        print(len(test_cases), " test cases passed for Square Root!")

    def test_division_method(self):
        calculator = Calculator()
        test_cases = read_csv("src/test/Unit Test Division.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.divide(int(test_case[1]), int(test_case[0])), float(test_case[2]))
        print(len(test_cases), " test cases passed for Division!")

    def test_results_property(self):
        calculator = Calculator()
        calculator.add(1, 2)
        self.assertEqual(calculator.result, 3)


if __name__ == '__main__':
    unittest.main()
