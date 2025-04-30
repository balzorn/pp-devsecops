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
basket = []

def print_catalogue():
    print("{:^4}".format("Код") + " " + "{:^14}".format("Товар") + "{:^7}".format("Цена"))
    for product in catalogue:
        print(f'{product["id"]:0>4} {product["title"]:.<14}{f'{product['price']:.2f}':.>7}$')

def print_menu():
    print

def main():
    print_catalogue()


if __name__ == "__main__":
    main()
