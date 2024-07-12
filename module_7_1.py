class Shop:
    __file_name = 'products.txt'

    # режим записи, если встретилось наименование
    # - ignore - пропускать (остается старое значение
    # - update - обновлять (записывает новое значение)
    __mode = ('ignore', 'update', 'append')

    def __init__(self):
        file = open(self.__file_name, 'w', encoding='utf-8')
        file.close()

    def get_products(self, *category):
        current_product = []
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            for line in file:
                current_product.append(Product(*line.replace('\n', '').split(', ')))
        if (len(category)) > 0:
            selected_product = []
            for c in category:
                selected_product.extend([p for p in current_product if p.category == c])
            return selected_product
        return current_product

    def print_products(self, *category):
        for p in self.get_products(*category):
            print(p)

    def add(self, *products, mode='ignore'):
        if mode not in self.__class__.__mode:
            mode = 'ignore'
        current_product = self.get_products()
        result = [0, 0, 0]

        for p in products:
            if p in current_product:
                if mode == 'update':
                    current_product[current_product.index(p)].wight = float(p.wight)
                elif mode == 'append':
                    current_product[current_product.index(p)].wight = (
                            float(current_product[current_product.index(p)].wight) + float(p.wight))
            else:
                current_product.append(p)
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for p in current_product:
                file.write(f'{p}\n')


class Product:
    __product_category = ('groceries', 'vegetables', 'fruits', 'dairy', 'bread')

    def __init__(self, name, wight, category):
        if category.lower() not in self.__class__.__product_category:
            raise ValueError('Invalid category')

        self.name = name
        self.wight = wight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.wight}, {self.category}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False


if __name__ == '__main__':
    shop = Shop()
    # добавляем продукты
    shop.add(Product('Бородинский хлеб', 0.400, 'bread'),
             Product('Молоко', 0.900, 'dairy'))

    print('Выводим список продуктов')
    shop.print_products()

    potato = Product('Картофель', 50.50, 'vegetables')
    spaghetti = Product('Спагетти', 3.4, 'Groceries')
    apple = Product('Яблоко', 37.80, 'fruits')
    milk = Product('Молоко', 1.50, 'dairy')
    # добавляем продукты с режимом по умолчанию 'ignore'
    shop.add(potato, spaghetti, apple, milk)
    print('\nВыводим список продуктов - Молоко не добавилось повторно')
    shop.print_products()

    # добавляем продукты в режиме 'update' (замещаем вес в уже существующих)
    shop.add(Product('Бородинский хлеб', 2.50, 'bread'),
             Product('Сыр "Пармезан"', 5, 'dairy'), mode='update')
    print('\nВыводим список продуктов - Вес Хлеба обновился')
    shop.print_products()

    # добавляем продукты в режиме 'append' (прибавляем вес в уже существующих)
    shop.add(Product('Молоко', 1.50, 'dairy'), mode='append')
    print('\nВыводим список продуктов с фильтрацией по категориям \'dairy\' и \'vegetables\' - '
          '\nВес Молока увеличился на 1.5')
    shop.print_products('dairy', 'vegetables')
