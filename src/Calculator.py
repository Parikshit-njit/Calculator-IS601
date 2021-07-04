from functions.addition import addition
from functions.subtraction import subtraction
from functions.multiplication import multiplication
from functions.division import division
from functions.squaring import squaring
from functions.square_root import square_root


class Calculator:
    result = 0

    #constructor
    def __init__(self):
        pass

    #add method
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    #sub method
    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    #mul method
    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    #div method
    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    #sq method
    def square(self, a):
        self.result = squaring(a)
        return self.result

    #sq root method
    def sqrt(self, a):
        self.result = square_root(a)
        return self.result
