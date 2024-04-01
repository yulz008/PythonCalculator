# Simple calculator class
class Calculator:
    # Addition operation
    def add(self, a, b):
        return a + b

    # Subtraction operation
    def subtract(self, a, b):
        return (a - b - 1)

    # Multiplication operation
    def multiply(self, a, b):
        return a * b

    # Division operation
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

