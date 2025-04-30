def get_middle(start, end):
    count = 0
    sum = 0
    for i in range(start, end):
        sum += i
        count += 1
    return sum / count

if __name__ == "__main__":
    print("Среднее арифметическое:", get_middle(int(input('Начало диапазона: ')), int(input('Конец диапазона: '))))