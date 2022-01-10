import unittest
from operation_sistem import OperationSistem
"""
Тесты
"""

class TestOperationSistem(unittest.TestCase):

    def test_name(self):
        self.assertEqual(OperationSistem.get_name(self), 'Linux')

    def test_release(self):
        self.assertEqual(OperationSistem.get_reliase(self), '#1 SMP Tue Dec 14 14:26:01 UTC 2021')

    def test_version(self):
        self.assertEqual(OperationSistem.get_version(self), '5.15.8-200.fc35.x86_64')

    def test_wrong_name(self):
        self.assertEqual(OperationSistem.get_name(self), 'Windows')

    def test_wrong_release(self):
        self.assertEqual(OperationSistem.get_reliase(self), 'Yesterday')

    def test_wrong_version(self):
        self.assertEqual(OperationSistem.get_version(self), '11')    