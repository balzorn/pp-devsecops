# 2. Дано расстояние в метрах. Найти число полных километров в нем.
def m_2_km(m: int):
    return m / 1000

#  3. Вывести на экран текст «Silence is golden». Каждое слово должно быть на новой строке.
def print_silence():
    print("Silence\nis\ngolden")

# 4. Дано число. Проверьте, четное оно или нет. Если четное выведите True,
# если нечетное – False. Решение должно быть в одну инструкцию
def chet(number: int):
    return True if number % 2 == 0 else False

# 5. Ввести год рождения в консоль. Вывести возраст. Текущий год используем 2025 в 
# явном виде, специальные функции для работы с датой использовать необязательно
CURRENT_YEAR = 2025
def get_yob() -> int:
    try:
        return int(input("Введите год рождения: "))
    except ValueError:
        print("Неверный формат года")

def print_age(yob: int):
    print(CURRENT_YEAR - yob)

def main():
    e_msg = "Неверный формат данных"
    try:
        print(f"Количество километров: {m_2_km(int(input('Введите метры: ')))}")
    except ValueError:
        print(e_msg)
    
    print_silence()

    try:
        print(f"Проверка на четность пройдена: {chet(int(input('Введите число для проверки: ')))}")
    except ValueError:
        print(e_msg)
    
    print_age(get_yob())



if __name__ == "__main__":
    main()
