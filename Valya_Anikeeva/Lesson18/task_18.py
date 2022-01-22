#1 Написать класс для работы с текущей операционной системой:
# Три метода(получить имя операционной системы, релиз операционной системы, версию OS)

import platform

class OperSystem:
    @staticmethod
    def name_os():
        return platform.system()

    @staticmethod
    def release_os():
        return platform.release()

    @staticmethod
    def version_os():
        return platform.version()

print(OperSystem.name_os(), OperSystem.release_os(), OperSystem.version_os())
