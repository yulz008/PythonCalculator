# calculator.py
# this implementation with static main operation and printing

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
if __name__ == "__main__":
    calc = Calculator()
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("Addition:", calc.add(a, b))
    print("Subtraction:", calc.subtract(a, b))
    print("Multiplication:", calc.multiply(a, b))
    try:
        print("Division:", calc.divide(a, b))
    except ValueError as e:
        print(e)
