import math

def main():
    print("Hello from Практическая работа. Модуль 1!")
    a = get_numeric('a')
    if a == 0:
        print('Это не квадратное уравнение (a = 0)')
    b = get_numeric('b')
    c = get_numeric('c')

    print(quadratic(a, b, c))

def get_numeric(v):
    while True:
        user_input = input(f'Введите значение числа (коэффициента) {v}: ')
        try:
            num = int(user_input)
            return num
        except ValueError:
            try:
                num = float(user_input)
                return num
            except ValueError:
                print('Ошибка ввода! Введите действительное число!')

def quadratic(a, b, c):
    D = math.pow(b, 2) - 4 * a * c

    if a == 0:
        return 'Это не квадратное уравнение (a = 0)'
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f'Уравнение имеет два корня: {x1=:.5f} и {x2=:.5f}'
    elif D == 0:
        x = -b / (2 * a)
        return f'Уравнение имеет один корень: {x=:.5f}'
    else:
        return f'Уравнение не имеет корней'

if __name__ == "__main__":
    main()
