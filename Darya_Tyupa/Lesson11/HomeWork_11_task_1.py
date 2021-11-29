from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @abstractmethod
    def get_age(self):
        return self.__age

    @abstractmethod
    def get_old(self):
        self.__age += 1

    @abstractmethod
    def walk(self):
        print(f'{self.name} походил/ла')

    @abstractmethod
    def voice(self):
        raise NotImplemented

    def __str__(self):  # сделала для удобства вывода каждого животного
        return f'{self.name} класса {self.__class__.__name__} '


class Birds(ABC):
    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @abstractmethod
    def get_age(self):
        return self.__age

    @abstractmethod
    def get_old(self):
        self.__age += 1

    @abstractmethod
    def fly(self):
        print(f'{self.name} полетал/ла')

    @abstractmethod
    def voice(self):
        raise NotImplemented

    def __str__(self):  # сделала для удобства вывода каждой птицы
        return f'{self.name} класса {self.__class__.__name__} '


class Pigs(Animals):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_old(self):
        self.__age += 1

    def walk(self):
        print(f'{self.name} походил/ла')

    def voice(self):
        print('хрю-хрю')


class Cows(Animals):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_old(self):
        self.__age += 1

    def walk(self):
        print(f'{self.name} походил/ла')

    def voice(self):
        print('му-му')


class Geese(Birds):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_old(self):
        self.__age += 1

    def fly(self):
        print(f'{self.name} полетал/ла')

    def voice(self):
        print('га-га-га')


class Chicken(Birds):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_old(self):
        self.__age += 1

    def fly(self):
        print(f'{self.name} полетал/ла')

    def voice(self):
        print('кудах-кудах')


class Farm:
    all_animals_and_birds = []  # здесь хранятся все животные на ферме

    @staticmethod
    def add_animals_or_birds(*args):
        for i in args:
            Farm.all_animals_and_birds.append(i)

    @staticmethod
    def __getitem__(index):
        return Farm.all_animals_and_birds[index]

    @staticmethod
    def __iter__():
        return iter(Farm.all_animals_and_birds)

    @staticmethod
    def get_old_all():
        for i in Farm.all_animals_and_birds:
            i.get_old()


# создаём животных и птиц
pig_1 = Pigs('Хрюша', 5)
pig_2 = Pigs('Винни', 3)

cow_1 = Cows('Бурёнка', 6)
cow_2 = Cows('Зорька', 2)

goose_1 = Geese('Серый', 1)
goose_2 = Geese('Белый', 4)

hen_1 = Chicken('Цыпа', 6)
hen_2 = Chicken('Коко', 2)

# добавляем животных и птиц на ферму
Farm.add_animals_or_birds(pig_1, cow_2, hen_2, goose_1, goose_2, pig_2, hen_1, cow_1)
# получем животное по индексу
print(Farm.all_animals_and_birds[3])
# получаем каждое животное на ферме
for i in Farm.all_animals_and_birds:
    print(i)
# увеличиваем возраст всех животных
Farm.get_old_all()

# увелчиваем возраст животного
pig_1.get_old()
# получаем возраст животного
print(pig_1.get_age())
# проверяем метод ходить
pig_1.walk()
# проверяем метод голос
pig_1.voice()


# пользовательский exception NotExistException (свой из класса MyException)
class MyException(Exception):
    """this class"""


class NoExistException(MyException):
    pass


# При обращении к несуществующему методу или атрибуту животного или птицы должен срабатывать пользовательский exception
try:
    pig_1.det_old()
except AttributeError as err:
    raise NoExistException(f'{err}')
