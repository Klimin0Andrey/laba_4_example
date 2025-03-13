class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def summary(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def product(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


if __name__ == "__main__":
    a, b = map(int, input("Введите значения переменных a, b: ").split())

    solution = Calculator(a, b)
    while True:
        your_choice = int(input("Введите команду Калькулятора: \n1)Сумма\n2)Минус\n3)Произведение\n4)Деление\n5)Выход\n"))
        match your_choice:
            case 1:
                print(solution.summary())
            case 2:
                print(solution.minus())
            case 3:
                print(solution.product())
            case 4:
                print(solution.divide())
            case 5:
                break