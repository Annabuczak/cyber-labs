class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b


class Extended(Calculator):
    def power(self, a, b):
        return a ** b

    def modulo(self, a, b):
        return a % b

    def floordiv(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a // b

    def percent(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return (a * b) / 100

    def average(self, a, b):
        return (a + b) / 2

    def absolute(self, a):
        return abs(float(a))

    def round(self, a, b):
        return round(float(a), b)

    def factorial(self, a):
        if a < 0:
            return "Error: Factorial is not defined for negative numbers"
        if a == 0 or a == 1:
            return 1
        result = 1
        for i in range(2, int(a) + 1):
            result *= i
        return result


def extended():
    print("\nExtended Calculator")
    while True:
        print("1. Power")
        print("2. Modulo")
        print("3. Floor Division")
        print("4. Percent")
        print("5. Average")
        print("6. Absolute Value")
        print("7. Round")
        print("8. Factorial")
        print("9. Exit")

        print("\nSelect an operation:")
        choice = input("Enter your choice: ")
        ext = Extended()

        if choice == "1":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            result = ext.power(a, b)
            print(result)
        elif choice == "2":
            a = float(input("Enter first amount:"))
            b = float(input("Enter second amount: "))
            result = ext.modulo(a, b)
            if isinstance(result, float) and result.is_integer():
                print(int(result))
            else:
                print(result)
            print(result)
        elif choice == "3":
            a = float(input("Enter first amount: "))
            b = float(input("Enter second amount: "))
            result = ext.floordiv(a, b)
            print(result)
        elif choice == "4":
            a = float(input("Enter first amount: "))
            b = float(input("Enter second amount: "))
            result = ext.percent(a, b)
            print(result)

        elif choice == "5":
            a = float(input("Enter first amount: "))
            b = float(input("Enter second amount: "))
            result = ext.average(a, b)
            print(result)

        elif choice == "6":
            a = float(input("Enter an amount: "))
            result = ext.absolute(a)
            print(result)

        elif choice == "7":
            a = float(input("Enter an amount: "))
            b = int(input("Enter number of decimal places: "))
            result = ext.round(a, b)
            print(result)

        elif choice == "8":
            a = int(input("Enter an integer: "))
            result = ext.factorial(a)
            print(result)

        elif choice == "9":
            break

        else:
            print("Exit")


def main():
    print("\nCalculator")
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Extended")  # Updated
        print("6. Exit")

        print("\nSelect an operation:")
        try:
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nExiting calculator...")
            break

        calc = Calculator()

        if choice == "1":
            a = float(input("Enter first amount: "))
            b = float(input("Enter second amount: "))
            result = calc.add(a, b)
            print(result)
        elif choice == "2":
            a = float(input("Enter first amount:"))
            b = float(input("Enter second amount: "))
            result = calc.subtract(a, b)
            print(result)
        elif choice == "3":
            a = float(input("Enter first amount: "))
            b = float(input("Enter second amount: "))
            result = calc.multiply(a, b)
            print(result)
        elif choice == "4":
            a = float(input("Enter first amount: "))
            b = float(input("Enter second amount: "))
            result = calc.divide(a, b)
            print(result)

        elif choice == "5":

            extended()
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
