class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read()

    def add(self, *products):
        with open(self.__file_name, 'a+', encoding='utf-8') as file:
            for p in products:
                file.seek(0)
                file_text = file.read()
                if p.name in file_text:
                    print(f'Продукт {p.name} уже есть в магазине')
                else:
                    file.write(f'{p}\n')


class Product:

    def __init__(self, name, wight, category):
        self.name = name
        self.wight = wight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.wight}, {self.category.lower().capitalize()}'


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
