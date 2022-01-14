import unittest
import info_OS


class PositiveCase(unittest.TestCase):  # Позитивные кейсы для моей ОС

    def test_name(self):
        self.assertEqual(info_OS.my_OS.get_system(), "Windows")

    def test_release(self):
        self.assertEqual(info_OS.my_OS.get_release(), "10")

    def test_version(self):
        self.assertEqual(info_OS.my_OS.get_version(), "10.0.17763")


class NegativeCase(unittest.TestCase):  # Негативные кейсы для моей ОС

    def test_name_negative(self):
        self.assertFalse(info_OS.my_OS.get_system() != "Windows")

    def test_release_negative(self):
        self.assertFalse(info_OS.my_OS.get_release() != "10")

    def test_version_negative(self):
        self.assertFalse(info_OS.my_OS.get_version() != "10.0.17763")
