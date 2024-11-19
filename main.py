class Calculator:
    def __init__(self):
        self.__operations = {
            "+": self.__add,
            "-": self.__subtract,
            "*": self.__multiply,
            "/": self.__divide
        }

    def __add(self, a, b):
        return a + b

    def __subtract(self, a, b):
        return a - b

    def __multiply(self, a, b):
        return a * b

    def __divide(self, a, b):
        if b == 0:
            raise ValueError("Помилка")
        return a / b

    def __validate_and_convert(self, value):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Не можливо конвертувати '{value}' на число")

    def calculate(self, a, b, operation):
        a = self.__validate_and_convert(a)
        b = self.__validate_and_convert(b)

        func = self.__operations.get(operation)
        if func is None:
            raise ValueError(f"Операція '{operation}' не підтримується")
        return func(a, b)


calculator = Calculator()

try:
    print(calculator.calculate(10, 5, "+"))
    print(calculator.calculate(10, 5, "-"))
    print(calculator.calculate(10, 5, "*"))
    print(calculator.calculate(10, 5, "/"))
    print(calculator.calculate(10, 0, "/"))
except ValueError as e:
    print(e)
