class Division:
    @staticmethod
    def div(a, b):
        try:
            c = a / b
            return c
        except:
            print("Division by 0 is not defined!!")