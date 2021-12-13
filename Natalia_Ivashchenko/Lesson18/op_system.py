import platform


class OpSystem:
    @staticmethod
    def get_name():
        return platform.system()

    @staticmethod
    def get_reliz():
        return platform.release()

    @staticmethod
    def get_versia():
        return platform.version()


print(OpSystem.get_name(), OpSystem.get_reliz(), OpSystem.get_versia())
