import unittest
from task_18 import OperSystem


class PositiveTests(unittest.TestCase):

    def test_os_name(self):
        self.assertEqual(OperSystem.name_os(), 'Linux')

    def test_os_release(self):
        self.assertEqual(OperSystem.release_os(), '5.13.0')

    def test_os_version(self):
        self.assertEqual(OperSystem.version_os(), '20.04.1')


class NegativeTests(unittest.TestCase):

    def test_failed_os_name(self):
        self.assertNotEqual(OperSystem.name_os(), 'Windows')

    def test_failed_os_release(self):
        self.assertNotEqual(OperSystem.release_os(), '10')

    def test_failed_os_version(self):
        self.assertNotEqual(OperSystem.version_os(), '10.10.1')
