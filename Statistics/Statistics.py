from calculator.Calculator import Calculator
from .Mean import mean


class Statistics(Calculator):
    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = mean(data)
        return self.result

