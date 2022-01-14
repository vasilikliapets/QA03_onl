import platform


class Info:

    def get_version(self):
        return platform.version()

    def get_release(self):
        return platform.release()

    def get_system(self):
        return platform.system()


my_OS = Info()

print(f"{my_OS.get_system()} \n{my_OS.get_release()} \n{my_OS.get_version()}")

"""Актуальные для моей ОС
Windows 
10 
10.0.17763
"""