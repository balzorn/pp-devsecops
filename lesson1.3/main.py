#  Напечатать таблицу умножения от 2 до 5
def print_table():
    t = list()
    for i in range(2, 10):
        t.append(list())
        for j in range(2, 6):
            t[i-2].append(f'{j} x {i} = {i * j}')
    for row in t:
        c = ""
        for cell in row:
            c += f"{cell:<15}"
        print(c)

# Вывести все простые числа от 2 до 100
def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def print_prime_numbers():
    for n in range(2, 101):
        if is_prime(n):
            print(n)


def main():
    print("Hello from lesson1-3!")
    print_table()
    print_prime_numbers()


if __name__ == "__main__":
    main()
