# Импортируем наш test runner - unittest
import unittest
import operation_system_info


# Создаем класс с тестами, наследуемся от класса TestCase
class TestPositiveOperationSystem(unittest.TestCase):


    # Метод для предусловия
    def setUp(self) -> None:
        print("Just for learning. This is precondition")

    # Метод для постусловия
    def tearDown(self) -> None:
        print("Just for learning. This is postcondition")


    def test_name_os(self):
        self.assertEqual(operation_system_info.OperationSystem.get_name_of_os(), 'Windows')

    def test_release_os(self):
        self.assertEqual(operation_system_info.OperationSystem.get_release_of_os(), '10')

    def test_version_os(self):
        self.assertEqual(operation_system_info.OperationSystem.get_version_of_os(), '10.0.19042')



class TestNegativeOperationSystem(unittest.TestCase):
    @unittest.expectedFailure
    def test_name_os(self):
        self.assertEqual(operation_system_info.OperationSystem.get_name_of_os(), 'MacOS')

    @unittest.expectedFailure
    def test_release_os(self):
        self.assertEqual(operation_system_info.OperationSystem.get_release_of_os(), '11')

    @unittest.expectedFailure
    def test_version_os(self):
        self.assertEqual(operation_system_info.OperationSystem.get_version_of_os(), '10.15')