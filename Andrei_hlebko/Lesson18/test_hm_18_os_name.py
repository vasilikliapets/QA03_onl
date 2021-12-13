import unittest

from Lesson18.hm_18_os_name import OsSystem


class TestSystemInformPositive(unittest.TestCase):

    def test_name_system(self):
        self.assertEqual(OsSystem.name_system(), "Darwin")

    def test_realise_system(self):
        self.assertEqual(OsSystem.realise_system(), "21.1.0")

    def test_os_version(self):
        self.assertEqual(OsSystem.os_vers(), "Darwin Kernel Version 21.1.0: Wed Oct 13 17:33:24 PDT 2021; "
                                             "root:xnu-8019.41.5~1/RELEASE_ARM64_T8101")


class TestSystemInformNegative(unittest.TestCase):

    def test_fail_name_system(self):
        self.assertEqual(OsSystem.name_system(), "Windows")

    def test_fail_realise_system(self):
        self.assertEqual(OsSystem.realise_system(), "1.2.3.4.5")

    def test_fail_os_version(self):
        self.assertEqual(OsSystem.os_vers(), "Windows 98")


if __name__ == '__main__':
    unittest.main()
