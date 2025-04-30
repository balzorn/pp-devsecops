def get_num(msg):
    while True:
        u_answ = input(f"Введите число {msg}: ")
        try:
            return int(u_answ)
        except ValueError:
            print(f'"{u_answ}" - не является числом')
        else:
            break

def get_numbers(n):
    num_negative = 0
    num_positive = 0
    num_null = 0
    for i in range(0, n):
        num = get_num(f'({i + 1} из {n})')
        if num < 0:
            num_negative += 1
        elif num > 0:
            num_positive += 1
        else:
            num_null += 1
    return (num_negative, num_null, num_positive)




if __name__ == "__main__":
    n = get_num("N")
    n_neg, n_null, n_pos = get_numbers(n)
    print(f'Чисел меньше нуля: {n_neg}\nНулей: {n_null}\nЧисел больше нуля: {n_pos}')
