import platform


class OS:
    @staticmethod
    def os_name():
        return platform.system()

    @staticmethod
    def os_release():
        return platform.release()

    @staticmethod
    def os_version():
        return platform.version()


print(OS.os_name(), OS.os_release(), OS.os_version())
