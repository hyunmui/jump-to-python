# Calculator.py

class Calculator:
    def __init__(self) -> None:
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


calc1 = Calculator()
calc2 = Calculator()

print(calc1.add(3))
print(calc1.add(4))
print(calc2.add(3))
print(calc2.add(7))

print(calc1.sub(2))
