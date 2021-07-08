from Calculator.Calculator import Calculator
from Mean import mean


class Statistics(Calculator):
    def __init__(self):
        super().__init__()

    def get_mean(self):
        self.result = mean(self.mean_list)

