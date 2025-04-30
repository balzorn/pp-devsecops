sports = ["лыжи", "теннис", "гиревой спорт"]

sports.append(input("Введите cвой любимый вид спорта: "))
sports.sort()
for s in sports:
    print(s)
