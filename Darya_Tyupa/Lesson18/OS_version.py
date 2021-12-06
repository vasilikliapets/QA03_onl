import platform


class OSVersion:

    @staticmethod
    def os_name():
        """This method returns the name of the OS"""
        return platform.system()

    @staticmethod
    def os_release():
        """This method returns release of the OS"""
        return platform.release()

    @staticmethod
    def os_version():
        """This method returns version of the OS"""
        return platform.version()
