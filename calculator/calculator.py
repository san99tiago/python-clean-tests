# SAMPLE CALCULATOR FOR EXPLAINING UNIT-TESTING IN OTHER SCRIPTS
# Santiago Garcia Arango

class Calculator:
    """
    Cool basic calculator to illustrate unit-testing in Python
    """

    def __init__(self):
        self.value = 0
        print("This amazing calculator initialized successfully")

    def add(self, x, y):
        """Add Method"""
        return x + y

    def subtract(self, x, y):
        """Subtract Method"""
        return x - y

    def multiply(self, x, y):
        """Multiply Method"""
        return x * y

    def divide(self, x, y):
        """Divide Method"""
        if y == 0:
            raise ValueError("You can not divide by zero, think twice")
        return x / y
