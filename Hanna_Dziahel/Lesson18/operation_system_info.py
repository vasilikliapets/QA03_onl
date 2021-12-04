# Импортируем модуль platform для дальнейшего получения информации об
# операционной системе
import platform

class OperationSystem:
    @staticmethod
    def get_name_of_os():
        return platform.system()

    @staticmethod
    def get_release_of_os():
        return platform.release()

    @staticmethod
    def get_version_of_os():
        return platform.version()

print(OperationSystem.get_name_of_os(), OperationSystem.get_release_of_os(), OperationSystem.get_version_of_os())
