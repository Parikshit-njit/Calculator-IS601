from src.Calculator import Calculator

cal = Calculator()

while True:
    print("Choose an option from the following:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")

    option = int(input().strip())

    if option == 1:
        print("Enter number 1:")
        a = int(input().strip())

        print("Enter number 2:")
        b = int(input().strip())
        print("Result is", cal.add(a, b))
    elif option == 2:
        print("Enter number 1:")
        a = int(input().strip())

        print("Enter number 2:")
        b = int(input().strip())
        print("Result is", cal.subtract(a, b))
    elif option == 3:
        print("Enter number 1:")
        a = int(input().strip())

        print("Enter number 2:")
        b = int(input().strip())
        print(cal.multiply(a, b))
    elif option == 4:
        print("Enter number 1:")
        a = int(input().strip())

        print("Enter number 2:")
        b = int(input().strip())
        print("Result is", cal.divide(a, b))
    elif option == 5:
        print("Enter number 1:")
        a = int(input().strip())
        print("Result is", cal.square(a))
    elif option == 6:
        print("Enter number 1:")
        a = int(input().strip())
        print("Result is", cal.sqrt(a))

    print("Exit :: Press 1 || Continue :: Press 0")
    exit_pressed = int(input().strip())
    if exit_pressed == 1:
        print("Bye!")
        break;


