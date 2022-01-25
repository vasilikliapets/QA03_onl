import unittest
import operSystem


class TestPositive(unittest.TestCase):
    def test_name(self):
        self.assertEqual(operSystem.OperationSystem.name_os(), "Windows")

    def test_release(self):
        self.assertEqual(operSystem.OperationSystem.release_os(), "10")

    def test_version(self):
        self.assertEqual(operSystem.OperationSystem.version_os(), "10.0.19041")


class TestNegative(unittest.TestCase):
    def test_name(self):
        self.assertNotEqual(operSystem.OperationSystem.name_os(), "Linux Ubuntu")

    def test_release(self):
        self.assertNotEqual(operSystem.OperationSystem.release_os(), "9")

    def test_version(self):
        self.assertNotEqual(operSystem.OperationSystem.version_os(), "20.04")
