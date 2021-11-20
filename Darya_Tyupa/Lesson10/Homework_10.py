class Flowers:
    def __init__(self, freshness, color, stalk_length):
        self.freshness = freshness
        self.color = color
        self.stalk_length = stalk_length

    def __str__(self):
        return f'{self.color} {self.__class__.__name__}'


class Rose(Flowers):
    price = 10

    def __init__(self, freshness, color, stalk_length):
        super().__init__(freshness, color, stalk_length)


class Tulip(Flowers):
    price = 7

    def __init__(self, freshness, color, stalk_length):
        super().__init__(freshness, color, stalk_length)


class Violet(Flowers):
    price = 15

    def __init__(self, freshness, color, stalk_length):
        super().__init__(freshness, color, stalk_length)


class Chamomile(Flowers):
    price = 5

    def __init__(self, freshness, color, stalk_length):
        super().__init__(freshness, color, stalk_length)


class WrappingPaper:
    price = 2

    def __str__(self):
        return f'{self.__class__.__name__}'


class Bouquets:
    def __init__(self, *flowers):  # конструктор который принимает тьюпл из цветов
        self.flowers = flowers

    def bouquet_price(self):
        """This function counts the total price of the bouquet"""
        total_price = 0
        for i in self.flowers:
            total_price += i.price
        return total_price

    def lifetime(self):
        """This function counts the lifetime of the bouquet"""
        days = 0  # общее количество дней
        count = 0  # количество цветов
        for i in self.flowers:
            if isinstance(i, Flowers):
                days += i.freshness
                count += 1
        return days / count  # делим общее количество дней на количество цветов и находим жизнь букета

    def sorting_by_freshness(self):
        """This function sorts the flowers in the bouquet by freshness and prints flowers in the right order"""
        flowers = []  # создаю лист чтобы закинуть в него только цветы (без аксессуаров)
        for i in self.flowers:
            if isinstance(i, Flowers):
                flowers.append(i)
        flowers = sorted(flowers, key=lambda i: i.freshness)  # сортировка по ключу свежесть
        for i in flowers:
            print(i)

    def sorting_by_color(self):
        """This function sorts the flowers in the bouquet by color and prints flowers in the right order"""
        flowers = []
        for i in self.flowers:
            if isinstance(i, Flowers):
                flowers.append(i)
        flowers = sorted(flowers, key=lambda i: i.color)
        for i in flowers:
            print(i)

    def sorting_by_length(self):
        """This function sorts the flowers in the bouquet by length and prints flowers in the right order"""
        flowers = []
        for i in self.flowers:
            if isinstance(i, Flowers):
                flowers.append(i)
        flowers = sorted(flowers, key=lambda i: i.stalk_length)
        for i in flowers:
            print(i)

    def sorting_by_price(self):
        """This function sorts all stuff in the bouquet by freshness and prints it in the right order"""
        flowers = sorted(list(self.flowers), key=lambda i: i.price)
        for i in flowers:
            print(i)

    def find_flowers_by_color(self, color):
        """This function prints flowers according to the specified color"""
        flowers = []  # создала пустой лист, для проверки есть ли такой цветок
        for i in self.flowers:
            if isinstance(i, Flowers):
                if i.color == color:
                    flowers.append(i)
                    print(i)
        if flowers == []:
            print('There is no such flower')

    def find_flowers_by_price(self, price):
        """This function prints stuff according to the specified price"""
        flowers = []
        for i in self.flowers:
            if i.price == price:
                flowers.append(i)
                print(i)
        if flowers == []:
            print('There is no such flower')

    def find_flowers_by_length(self, length):
        """This function prints stuff according to the specified length"""
        flowers = []
        for i in self.flowers:
            if isinstance(i, Flowers):
                if i.stalk_length == length:
                    flowers.append(i)
                    print(i)
        if flowers == []:
            print('There is no such flower')

    def find_flowers_by_freshness(self, freshness):
        """This function prints stuff according to the specified freshness"""
        flowers = []
        for i in self.flowers:
            if isinstance(i, Flowers):
                if i.freshness == freshness:
                    flowers.append(i)
                    print(i)
        if flowers == []:
            print('There is no such flower')

    def __contains__(self, flower):
        return flower in self.flowers

    def __getitem__(self, index):
        return self.flowers[index]

    def __iter__(self):
        return iter(self.flowers)


# создаём цветы(экземпляры) классов
red_rose = Rose(10, 'Red', 25)
white_rose = Rose(10, 'White', 20)
pink_rose = Rose(3, 'Pink', 20)

white_chamomile = Chamomile(7, 'White', 10)
blue_chamomile = Chamomile(7, 'Blue', 10)

purple_violet = Violet(10, 'Purple', 6)
white_violet = Violet(9, 'White', 7)

white_tulip = Tulip(8, 'White', 10)
red_tulip = Tulip(5, 'Red', 9)
purple_tulip = Tulip(4, 'Purple', 11)
yellow_tulip = Tulip(8, 'Yellow', 10)

# создаём упаковочную бумагу
wrapping_paper = WrappingPaper()

# создаём букет
bouquet_1 = Bouquets(purple_tulip, red_tulip, yellow_tulip, white_rose, blue_chamomile, wrapping_paper)

# выводим информацию о цветке
print(red_rose)
print(white_chamomile)
print(white_tulip)

# узнаём цену букета
print(bouquet_1.bouquet_price())

# узнаём время увядания букета
print(bouquet_1.lifetime())

# проверяем сортировки
bouquet_1.sorting_by_freshness()
bouquet_1.sorting_by_price()
bouquet_1.sorting_by_color()
bouquet_1.sorting_by_length()

# находим цветы по параметрам
bouquet_1.find_flowers_by_color('Red')
bouquet_1.find_flowers_by_price(10)
bouquet_1.find_flowers_by_length(10)
bouquet_1.find_flowers_by_freshness(10)

# проверяем есть ли цветок в букете
print(white_rose in bouquet_1)
print(white_tulip in bouquet_1)
# находим цветок по индексу
print(bouquet_1[1])
# итерируемся по букету
for i in bouquet_1:
    print(i)
