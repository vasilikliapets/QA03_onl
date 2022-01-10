import platform
"""
Класс для работы с информацией по ОС
"""

class OperationSistem:      # использую "i" в слове "system" для избежания возможных конфликтов. 

    def get_name(self):
        return platform.system()

    def get_reliase(self):
        return platform.version()  # поменял местами release и version для корректного вывода информации(не знаю почему у меня так выводит)

    def get_version(self):
        return platform.release()


sistem = OperationSistem()
print(sistem.get_name())
print(sistem.get_reliase())
print(sistem.get_version())
