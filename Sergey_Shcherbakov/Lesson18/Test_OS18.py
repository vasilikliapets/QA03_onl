import unittest
import Info_OS18


class TestPositive(unittest.TestCase):
    def test_name(self):
        self.assertEqual(Info_OS18.OS.os_name(), "Windows")

    def test_release(self):
        self.assertEqual(Info_OS18.OS.os_release(), "10")

    def test_version(self):
        self.assertEqual(Info_OS18.OS.os_version(), "10.0.19044")


class TestNegative(unittest.TestCase):
    def test_name(self):
        self.assertNotEqual(Info_OS18.OS.os_name(), "Mac OS")

    def test_release(self):
        self.assertNotEqual(Info_OS18.OS.os_release(), "12")

    def test_version(self):
        self.assertNotEqual(Info_OS18.OS.os_version(), "12.2")
