class Flowers:

    def __init__(self, fresh, color, flower_lenght):  #
        self.fresh = fresh
        self.color = color
        self.flower_lenght = flower_lenght

    def __str__(self):
        return f"{self.color} {self.__class__.__name__}"


class Roses(Flowers):
    price = 20

    def __init__(self, fresh, color, flower_lenght):
        super().__init__(fresh, color, flower_lenght)


class Tulips(Flowers):
    price = 10

    def __init__(self, fresh, color, flower_lenght):
        super().__init__(fresh, color, flower_lenght)


class Violets(Flowers):
    price = 8

    def __init__(self, fresh, color, flower_lenght):
        super().__init__(fresh, color, flower_lenght)


class Cammomile(Flowers):
    price = 7

    def __init__(self, fresh, color, flower_lenght):
        super().__init__(fresh, color, flower_lenght)


class Paper_flower:
    price = 1


class Bouquet:  # букет цветов
    def __init__(self, *flowers):
        self.bouquet = flowers

    def __getitem__(self, index):  # Узнать есть ли цветок в букете по индексу
        return self.bouquet[index]

    def price_bouquet(self):  # Вывод Стоимости букета
        total = 0
        for i in self.bouquet:
            total += i.price
        return f"Итоговая цена букета составляет {total} руб."

    def freshness_bouquet(self):  # Определяем время его увядания по среднему времени жизни всех цветов в букете
        total_fresh = 0
        count_flower = 0
        for i in self.bouquet:
            if isinstance(i, Flowers):
                total_fresh += i.fresh
                count_flower += 1  # Считаем именно количество цветов в букете что бы на это число разделить
        print(f"Средняя свежесть букета составляет {total_fresh // count_flower} дня")

    def print_all_flowers_in_bouquet(self):  # Вывод каждого цветка в букете
        for flowers in self.bouquet:
            if isinstance(flowers, Flowers):
                print(flowers)

    # Поиск цветов в букете по определенным параметрам

    def find_flower_by_length(self, lenght):  # По длине
        for i in self.bouquet:
            if isinstance(i, Flowers):
                if i.flower_lenght == lenght:
                    print(i)

    def find_flower_by_color(self, color):  # По цвету
        for i in self.bouquet:
            if isinstance(i, Flowers):
                if i.color == color:
                    print(i)

    def find_flower_by_fresh(self, fresh):  # По свежести
        for i in self.bouquet:
            if isinstance(i, Flowers):
                if i.fresh == fresh:
                    print(i)

    def find_flower_by_price(self, price):  # По цене
        for i in self.bouquet:
            if isinstance(i, Flowers):
                if i.price == price:
                    print(i)

    def __contains__(self, obj):
        return obj in self.bouquet

    # Сортировка цветов в букете на основе различных параметров
    def sorted_by_color(self):  # Сортировка букета по параметрам.(свежесть/цвет/длина стебля/стоимость…
        colors_sorted = []
        for i in self.bouquet:
            if isinstance(i, Flowers):
                colors_sorted.append(i)
        # colors_sorted = sorted(colors_sorted, key=lambda x: x.color)#Второй вариант
        colors_sorted.sort(key=lambda x: x.color)
        for i in colors_sorted:
            print(f"Сортировка по цвету: {i}: {i.color} ")

    def sorted_by_flower_lenght(self):  # Сортировка букета по параметрам.(свежесть/цвет/длина стебля/стоимость…
        lenght_sorted = []
        for i in self.bouquet:
            if isinstance(i, Flowers):
                lenght_sorted.append(i)
        # lenght_sorted = sorted(lenght_sorted, key=lambda x: x.flower_lenght)-#Второй вариант
        lenght_sorted.sort(key=lambda x: x.flower_lenght)
        for i in lenght_sorted:
            print(f"Длина цветка {i} в букете составляет: {i.flower_lenght} см")

    def sorted_by_fresh(self):  # Сортировка букета по параметрам.(свежесть/цвет/длина стебля/стоимость…
        fresh_sorted = []
        for i in self.bouquet:
            if isinstance(i, Flowers):
                fresh_sorted.append(i)
        # fresh_sorted = sorted(fresh_sorted, key=lambda x: x.fresh)#Второй вариант
        fresh_sorted.sort(key=lambda x: x.fresh)
        for i in fresh_sorted:
            print(f"Свежесть цветка {i} в букете составляет: {i.fresh} дней")

    def sorted_by_price(self):  # Сортировка букета по параметрам.(свежесть/цвет/длина стебля/стоимость…
        price_sorted = []
        for i in self.bouquet:
            if isinstance(i, Flowers):
                price_sorted.append(i)
        # price_sorted = sorted(price_sorted, key=lambda x: x.price)#Второй вариант
        price_sorted.sort(key=lambda x: x.price)
        for i in price_sorted:
            print(i, f"Цена цветка: {i.price} руб")


#####СОЗДАНИЕ
# создаём цветы со значениями
rose1 = Roses(1, "Red", 30)
violet1 = Violets(2, "Purple", 10)
cammomile = Cammomile(3, "Yellow", 15)
tulips = Tulips(1, "Orange", 20)

# Создаём акссесуары, например бумага
paper1 = Paper_flower()

# Создаем букет
bouquet_1 = Bouquet(tulips, rose1, violet1, cammomile, paper1)
bouquet_2 = Bouquet(rose1, violet1, cammomile)
bouquet_3 = Bouquet(violet1, cammomile)  # без розы
bouquet_4 = Bouquet(rose1, cammomile, paper1)  # без фиалок(violet)

#####ВЫВОДЫ

# # Выводим текст названия цвета и типа цветка
# print(rose1)  # Red Roses


# # Выводим стоимость букета
# print(Bouquet.price_bouquet(bouquet_2))-Как правильнее вызывать???
# print(bouquet_1.price_bouquet())          #или так  правильнее??


# # узнаем есть ли цветок в букете
# print(rose1 in bouquet_2)  # True
# # узнаем есть ли цветок в букете по Индексу
# print(bouquet_1[2])


# # Выводит каждый Цветок из букета
# bouquet_1.print_all_flowers_in_bouquet()

# Поиск цветка в букете с передачей параметра
# bouquet_1.find_flower_by_color("Red")#Red Roses
# bouquet_1.find_flower_by_length(10) #Purple Violets
# bouquet_1.find_flower_by_fresh(1)#Red Roses and Orange Tulips
# bouquet_1.find_flower_by_price(10)#Orange Tulips

# #Определяем время его увядания по среднему времени жизни всех цветов в букете
# bouquet_2.freshness_bouquet()


##Отсортированный список по цвету
# bouquet_1.sorted_by_color()
# bouquet_1.sorted_by_flower_lenght()
# bouquet_1.sorted_by_fresh()
# bouquet_1.sorted_by_price()
