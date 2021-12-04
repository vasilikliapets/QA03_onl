class Flowers:  # Класс цветов с общими параметрами

    def __init__(self, freshness, color, length_of_stem):
        self.freshness = freshness
        self.color = color
        self.length_of_stem = length_of_stem

    def __str__(self):
        return f"{self.color} {self.__class__.__name__}"


class Roses(Flowers):  # класс роз
    price = 5

    def __init__(self, freshness, color, length_of_stem):
        super().__init__(freshness, color, length_of_stem)


class Tulips(Flowers):
    price = 3

    def __init__(self, freshness, color, length_of_stem):
        super().__init__(freshness, color, length_of_stem)


class Violets(Flowers):
    price = 3

    def __init__(self, freshness, color, length_of_stem):
        super().__init__(freshness, color, length_of_stem)


class Chamomiles(Flowers):
    price = 3

    def __init__(self, freshness, color, length_of_stem):
        super().__init__(freshness, color, length_of_stem)


class Paper:
    price = 2


rose_1 = Roses(2, "Red", 6)
rose_2 = Roses(3, "White", 5)
tulip_1 = Tulips(2, "Pink", 5)
tulip_2 = Tulips(4, "Red", 5)
violet_1 = Violets(1, "Blue", 3)
violet_2 = Violets(2, "Black", 4)
chamomile_1 = Chamomiles(5, "White", 5)
chamomile_2 = Chamomiles(4, "White", 6)
paper_1 = Paper()
paper_2 = Paper()


class Bouquet:

    def __init__(self, *kwargs):  # создание букета из цветов и аксесуаров
        self.bouquet = kwargs

    def get_price(self):  # подсчет общей цены букета
        bouquet_price = 0
        for i in self.bouquet:
            bouquet_price += i.price
        return bouquet_price

    def get_freshness(self):  # получение средней свежести всех цветов
        freshness = 0
        count = 0
        for i in self.bouquet:
            if isinstance(i, Flowers):  # ограничение на учет свежести только цветов
                freshness += i.freshness
                count += 1
        return round(freshness / count, 1)  # округление до одного знака после запятой

    def sort_by_key(self, key):  # сорировка по ключу freshness/color/price и тд
        list_of_flowers = []
        for i in self.bouquet:
            if isinstance(i, Flowers):
                list_of_flowers.append(i)
        if key == 'freshness':
            list_of_flowers = sorted(list_of_flowers, key=lambda i: i.freshness)
            for i in list_of_flowers:
                print(i)
        elif key == 'color':
            list_of_flowers = sorted(list_of_flowers, key=lambda i: i.color)
            for i in list_of_flowers:
                print(i)
        elif key == 'length_of_stem':
            list_of_flowers = sorted(list_of_flowers, key=lambda i: i.length_of_stem)
            for i in list_of_flowers:
                print(i)
        elif key == 'price':
            list_of_flowers = sorted(list_of_flowers, key=lambda i: i.price)
            for i in list_of_flowers:
                print(i)

    def filter_by_color(self, key):  # фильтр по цвету
        list_of_flowers = []
        for i in self.bouquet:
            if isinstance(i, Flowers):
                list_of_flowers.append(i)
        list_of_flowers = filter(lambda i: key in i.color, list_of_flowers)
        for i in list_of_flowers:
            print(i)

    def filter_by_price(self, key):  # посик по цене
        list_of_flowers = []
        li_2 = []
        for i in self.bouquet:
            if isinstance(i, Flowers):
                list_of_flowers.append(i)
        for i in list_of_flowers:
            if i.price == key:
                li_2.append(i)
        for i in li_2:
            print(i)

    def __contains__(self, item):  # проверка вхождения цветка в букет
        return item in self.bouquet

    def __getitem__(self, item):  # поиск по индексу
        return self.bouquet[item]

    def __iter__(self):  # итератор по элементам
        return iter(self.bouquet)


b_1 = Bouquet(rose_1, rose_2, violet_1, paper_1, tulip_1, tulip_2)

b_1.sort_by_key('price')
print("--")
b_1.filter_by_color('Red')
print("--")
b_1.filter_by_price(5)
