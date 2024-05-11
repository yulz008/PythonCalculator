import sys

# Simple calculator class
class Calculator:
    # Addition operation
    def add(self, a, b):
        return a + b

    # Subtraction operation
    def subtract(self, a, b):
        return a - b

    # Multiplication operation
    def multiply(self, a, b):
        return a * b

    # Division operation
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

# Main application code
def main():
    calc = Calculator()

    if len(sys.argv) < 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        print("Operations: add, subtract, multiply, divide")
        return

    operation = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if operation == "add":
        print("Addition:", calc.add(a, b))
    elif operation == "subtract":
        print("Subtraction:", calc.subtract(a, b))
    elif operation == "multiply":
        print("Multiplication:", calc.multiply(a, b))
    elif operation == "divide":
        try:
            print("Division:", calc.divide(a, b))
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation. Use add, subtract, multiply, or divide.")

if __name__ == "__main__":
    main()
