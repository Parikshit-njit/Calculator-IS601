import unittest
from Calculator import Calculator
from CsvReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition_method(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Addition.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.add(int(test_case[0]), int(test_case[1])), int(test_case[2]))
        print(len(test_cases), " TestFiles cases passed for Addition!")

    def test_multiplication_method(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Multiplication.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.multiply(int(test_case[0]), int(test_case[1])), int(test_case[2]))
        print(len(test_cases), " TestFiles cases passed for Multiplication!")

    def test_subtraction_method(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Subtraction.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.subtract(int(test_case[1]), int(test_case[0])), int(test_case[2]))
        print(len(test_cases), " TestFiles cases passed for Subtraction!")

    def test_squaring_method(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Square.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.square(int(test_case[0])), int(test_case[1]))
        print(len(test_cases), " TestFiles cases passed for Squaring!")

    def test_square_root_method(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Square Root.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.sqrt(int(test_case[0])), float(test_case[1]))
        print(len(test_cases), " TestFiles cases passed for Square Root!")

    def test_division_method(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Division.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.divide(int(test_case[1]), int(test_case[0])), float(test_case[2]))
        print(len(test_cases), " TestFiles cases passed for Division!")

    def test_results_property_add(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Addition.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.add(int(test_case[1]), int(test_case[0])), calculator.result)
        print("Test cases (Addition) static variable :: result passed!")

    def test_results_property_sub(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Subtraction.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.subtract(int(test_case[1]), int(test_case[0])), calculator.result)
        print("Test cases (Subtraction) static variable :: result passed!")

    def test_results_property_mul(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Multiplication.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.multiply(int(test_case[1]), int(test_case[0])), calculator.result)
        print("Test cases (Multiplication) static variable :: result passed!")

    def test_results_property_div(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Division.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.divide(int(test_case[1]), int(test_case[0])), calculator.result)
        print("Test cases (Division) static variable :: result passed!")

    def test_results_property_square(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Square.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.square(int(test_case[0])), calculator.result)
        print("Test cases (Squaring) static variable :: result passed!")

    def test_results_property_square_root(self):
        calculator = Calculator()
        test_cases = CsvReader("src/TestFiles/Unit Test Square Root.csv")
        for test_case in test_cases:
            self.assertEqual(calculator.sqrt(int(test_case[0])), calculator.result)
        print("Test cases (Square Root) static variable :: result passed!")


if __name__ == '__main__':
    unittest.main()
