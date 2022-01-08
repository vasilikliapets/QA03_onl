from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def __init__(self, name, age):  # конструктор животных
        self.name = name
        self.__age = age

    @abstractmethod
    def get_age(self):  # получить возраст
        return self.__age

    @abstractmethod
    def set_old(self):  # увеличить возраст на 1
        self.__age += 1

    @abstractmethod
    def move(self):  # метод хождения
        print(f'топ-топ')

    @abstractmethod
    def voice(self):  # голос
        raise NotImplemented


class Birds(ABC):

    @abstractmethod
    def __init__(self, name, age):  # конструктор птиц
        self.name = name
        self.__age = age

    @abstractmethod
    def get_age(self):  # получить возраст
        return self.__age

    @abstractmethod
    def set_old(self):  # увеличить возраст на единицу
        self.__age += 1

    @abstractmethod
    def fly(self):  # метод летать
        print(f'звуки полета')

    @abstractmethod
    def voice(self):  # голос
        raise NotImplemented


class Pigs(Animals):  # класс Свиньи от животных

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_old(self):
        self.__age += 1

    def move(self):
        print(f'топ-топ')

    def voice(self):
        print('хрю')


class Cows(Animals):  # класс коров

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_old(self):
        self.__age += 1

    def move(self):
        print(f'топ-топ')

    def voice(self):
        print('муу')


class Geese(Birds):  # класс гусей от птиц

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_old(self):
        self.__age += 1

    def fly(self):
        print(f'звуки полета')

    def voice(self):
        print('га')


class Chicken(Birds):  # класс курицы

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_old(self):
        self.__age += 1

    def fly(self):
        print(f'звуки полета')

    def voice(self):
        print('ко')


class Farm():
    all_farm = []  # все животные/птицы фермы

    @staticmethod
    def add(*args):
        for i in args:
            Farm.all_farm.append(i)

    @staticmethod
    def set_all_old():
        for i in Farm.all_farm:
            i.set_old()

    def __getitem__(self, item):  # поиск по индексу
        return self.all_farm[item]

    def __iter__(self):  # итератор по элементам
        return iter(self.all_farm)


class MyException(Exception):
    pass


pig_1 = Pigs('свинья 1', 2)
cow_1 = Cows('корова 1', 3)
geese_1 = Geese('гусь', 1)


class NotExistException(MyException):
    pass


try:
    pig_1.set_ld()
except AttributeError as err:
    raise NotExistException(f'Error: {err}')


