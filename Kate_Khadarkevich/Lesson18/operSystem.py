import platform


class OperationSystem:

    @staticmethod
    def name_os():
        return platform.system()

    @staticmethod
    def release_os():
        return platform.release()

    @staticmethod
    def version_os():
        return platform.version()


print(OperationSystem.name_os(), OperationSystem.release_os(), OperationSystem.version_os())
