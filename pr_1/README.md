# Практическая работа. Модуль 1

## Задача

Создать программу на Python для решения квадратного уравнения.

## Описание задания

Программа должна попросить пользователя ввести коэффициенты квадратного уравнения `a`, `b` и `c`:

```
a * x^2 + b * x + c = 0
```

### Исключения

- Программа должна коррекно обработать ввод пользователем:
  - целых чисел
  - чисел с десятичными знаками
- При корректном вводе пользователя программа не должна выдавать программных ошибок, типа деления на 0
- Программа может не обрабатывать:
  - некорректный ввод пользователем коэффициентов в виде текста, например `KM3ауЫ`

### Вывод

На выходе программа должна вывести все возможные корни уравнения с точностью 5 знаков после запятой.

> Примеры вывовда:
>
> - Уравнение имеет два корня: 5.8534 и -4,0000
> - Уравнение имеет один корень: 8,8534
> - Уравнение не имеет корней
> - Это не квадратное уравнение. (Если пользователь ввёл a равное 0)
