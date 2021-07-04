from functions.addition import addition


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
        self.result = a - b
        return self.result

    #mul method
    def multiply(self, a, b):
        self.result = a * b
        return self.result

    #div method
    def divide(self, a, b):
        self.result = a / b
        return self.result

    #sq method
    def square(self, a):
        self.result = a * a
        return self.result

    #sq root method
    def sqrt(self, a):
        self.result = pow(a, 0.5)
        return self.result
