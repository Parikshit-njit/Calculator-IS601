from functions.addition import Addition
from functions.subtraction import Subtraction
from functions.multiplication import Multiplication
from functions.division import Division
from functions.squaring import Squaring
from functions.square_root import SquareRoot


class Calculator:
    result = 0

    #constructor
    def __init__(self):
        pass

    #add method
    @classmethod
    def add(self, a, b):
        self.result = Addition.add(a, b)
        return self.result

    #sub method
    @classmethod
    def subtract(self, a, b):
        self.result = Subtraction.sub(a, b)
        return self.result

    #mul method
    @classmethod
    def multiply(self, a, b):
        self.result = Multiplication.mul(a, b)
        return self.result

    #div method
    @classmethod
    def divide(self, a, b):
        self.result = Division.div(a, b)
        return self.result

    #sq method
    @classmethod
    def square(self, a):
        self.result = Squaring.squaring(a)
        return self.result

    #sq root method
    @classmethod
    def sqrt(self, a):
        self.result = SquareRoot.square_root(a)
        return self.result
