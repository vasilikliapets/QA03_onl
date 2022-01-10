from abc import ABC


class Birds(ABC):
    def __init__(self, name, ages):
        self.name = name
        self._ages = ages

    def get_age(self):
        return self._ages

    @staticmethod
    def fly():
        print("Я лечуу!")

    def grow_old(self):
        self._ages += 1

    @staticmethod
    def voice():
        print("Чык чырык")


class Animals(ABC):
    def __init__(self, name, ages):
        self.name = name
        self._ages = ages

    def get_age(self):
        return self._ages

    @staticmethod
    def move():
        print("Я хожу!")

    def grow_old(self):
        self._ages += 1

    @staticmethod
    def voice():
        print("Рррррр")


class Pig(Animals):
    def voice(self):
        print("Хрю")


class Goose(Birds):
    def voice(self):
        print("Радио Га Га")


class Chicken(Birds):
    def voice(self):
        print("Ко-Ко-Ко")


class Cow(Animals):
    def voice(self):
        print("Myyyyy")


class Ferm:
    spis_all_animals_and_birds = []

    @classmethod
    def add_all_animals_and_birds(cls, *args):
        for i in args:
            Ferm.spis_all_animals_and_birds.append(i)

    @classmethod
    def __getitem__(cls, index):
        return cls.spis_all_animals_and_birds[index]

    def __contains__(self, index):
        return index.name in self.spis_all_animals_and_birds

    @staticmethod
    def print_all_animals():
        for animal in Ferm.spis_all_animals_and_birds:
            print(animal.name)

    @staticmethod
    def add_all_one_year():
        for i in Ferm.spis_all_animals_and_birds:
            i.grow_old()


class MyException(Exception):
    pass


# Birds
chicken = Chicken("Chic", 2)
pigeon = Birds("Pigi", 5)
stork = Birds("Stork", 10)
goose = Goose("Gusik", 4)

# Animals
pig = Pig("Pepa", 3)
bear = Animals("Misha", 8)
cat = Animals("Barbos", 1)
cow = Cow("Burenka", 2)

# Созданных животных заносим в ферму +
Ferm.add_all_animals_and_birds(cat, chicken, pig, pigeon, goose, stork)


# # Выводим всех кто на ферме +
# Ferm.print_all_animals()

# # #Есть ли то или иное животное в списке на ферме
# print(cat in Ferm.spis_all_animals_and_birds)#True +
# print(bear in Ferm.spis_all_animals_and_birds)#False +


# # Вывести любое животное на ферме по индексу
# print(Ferm.spis_all_animals_and_birds[2].name)  # Выводит имя животного +

# Получить возраст животного
# print(pig.get_age())# +


# Добавить всем животным на ферме +1 год. +
# Ferm.add_all_one_year()

# проверка обращения к несуществующему методу c Ошибкой NotExistException
class NotExistException(MyException):
    pass


try:
    Ferm.print_hello()
except AttributeError as err:
    raise NotExistException(f"Your mistake > {err}")
