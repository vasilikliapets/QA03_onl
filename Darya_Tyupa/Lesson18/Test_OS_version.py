import unittest
from OS_version import OSVersion


class PositiveTests(unittest.TestCase):

    def test_os_name(self):
        self.assertEqual(OSVersion.os_name(), 'Windows')

    def test_os_release(self):
        self.assertEqual(OSVersion.os_release(), '10')

    def test_os_version(self):
        self.assertEqual(OSVersion.os_version(), '10.0.19042')


class NegativeTests(unittest.TestCase):

    def test_failed_os_name(self):
        self.assertNotEqual(OSVersion.os_version(), 'Linux')

    def test_failed_os_release(self):
        self.assertNotEqual(OSVersion.os_release(), '7')

    def test_failed_os_version(self):
        self.assertNotEqual(OSVersion.os_version(), '10.0.190')
