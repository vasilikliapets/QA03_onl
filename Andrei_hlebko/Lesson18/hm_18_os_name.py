import platform


class OsSystem:
    def name_system():
        """
        The function return system name
        """
        return platform.system()

    def realise_system():
        """
        The function return system realise
        """
        return platform.release()

    def os_vers():
        """
        The function return system version
        """
        return platform.version()
