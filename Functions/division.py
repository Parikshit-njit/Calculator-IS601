class Division:
    @staticmethod
    def div(a, b):
        try:
            c = a / b
            return c
        except ZeroDivisionError:
            return None