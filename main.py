from math import sqrt


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

    def square_root(self):
        value = input("Корень какого числа, вы хотите вычислить a или b? ")
        if value == 'a':
            return sqrt(self.x)
        else:
            return sqrt(self.y)

    def exponentiation(self):
        return self.x ** self.y


if __name__ == "__main__":
    a, b = map(int, input("Введите значения переменных a, b: ").split())

    solution = Calculator(a, b)
    while True:
        your_choice = int(input(
            "Введите команду Калькулятора: \n"
            "1)Сумма\n"
            "2)Минус\n"
            "3)Произведение\n"
            "4)Деление\n"
            "5)Квадратный корень\n"
            "6)Возведение в степень\n"
            "7)Выход\n"))

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
                print(solution.square_root())
            case 6:
                print(solution.exponentiation())
            case 7:
                break
