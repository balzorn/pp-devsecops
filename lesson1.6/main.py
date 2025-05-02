catalogue = [
    {
        "id": 10,
        "title": "Product10",
        "price": 9.99
    },
    {
        "id": 21,
        "title": "Product21",
        "price": 23.50
    },
    {
        "id": 32,
        "title": "Product32",
        "price": 0.23
    }
]
basket = [
    {
        "id": 21,
        "count": 5
    }
]

def add_order(id):
    for record in basket:
        if record['id'] == id:
            record['count'] += 1
            return
    basket.append({"id": id, "count": 1})

def find_product(id):
    for product in catalogue:
        if product['id'] == id:
            return product
    return None


def print_basket():
    print(f'\n{f' ':=>4}КОРЗИНА ТОВАРОВ{f' ':=<29}')
    print(f'{'Код':>4} {'Товар':<10} {'Заказ (шт)':>10} {'Цена/шт':>10} {'Сумма':>10}')
    for record in basket:
        product = find_product(record['id'])
        if product is not None:
            print(f'{record['id']:>4} {product['title']:<10} {record['count']:>10} {f'{product['price']:.2f}$':>10} {f'{product['price'] * record['count']:.2f}$':>10}')
    print(f'{f'':=>48}')

def print_catalogue():
    print(f'\n{f' ':=>4}КАТАЛОГ ТОВАРОВ{f' ':=<7}')
    print(f'{'Код':>4} {'Товар':<10} {'Цена':>10}')
    for product in catalogue:
        print(f'{product["id"]:>4} {product["title"]:<10} {f'{product['price']:.2f}$':>10}')
    print(f'{'':=>26}')

def print_menu():
    print(f'\n{f' ':=>4}МЕНЮ{f' ':=<25}')
    print(f'1. Вывести все товары каталога\n2. Добавить товар в корзину по id\n3. Вывести корзину\n4. Выход')

def get_product_id():
    while True:
        try:
            id = int(input('Введите код товара: '))
            if find_product(id) is None:
                print('Данный код товара не соответствует ни одному товару!')
                continue
            return id
        except ValueError:
            print("Неверный код товара!")
            continue
        

def main():
    while True:
        print_menu()
        try:
            answ = int(input('\nВведите номер меню: '))
        except ValueError:
            print("Введите действительный номер меню!")
            continue
        match answ:
            case 1:
                print_catalogue()
            case 2:
                add_order(get_product_id())
                print('Товар добавлен!')
                print_basket()
            case 3:
                print_basket()
            case 4:
                print('Удачи!')
                break
            case _:
                print('Нет такого пункта меню!')

if __name__ == "__main__":
    main()
