"""Module providing a function printing python version."""
# Simple calculator class
class Calculator:
    """Calculator Class."""
    # Addition operation
    def add(self, a, b):
        """Addition Operation"""
        return a + b

    # Subtraction operation
    def subtract(self, a, b):
        """Subtraction Operation"""
        return a - b + 2


    # Multiplication operation
    def multiply(self, a, b):
        """Multiplication Operation"""
        return a * b

    # Division operation
    def divide(self, a, b):
        """Division Operation"""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
