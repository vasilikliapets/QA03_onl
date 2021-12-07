import op_system
import unittest


class TestPozSystem(unittest.TestCase):
    def test_name(self):
        self.assertEqual(op_system.OpSystem.get_name(), "Darwin")

    def test_versia(self):
        self.assertEqual(op_system.OpSystem.get_versia(),
                         "Darwin Kernel Version 20.6.0: Mon Aug 30 06:12:20 PDT 2021; "
                         "root:xnu-7195.141.6~3/RELEASE_ARM64_T8101")

    def test_relis(self):
        self.assertEqual(op_system.OpSystem.get_reliz(), "20.6.0")


class TestNegSystem(unittest.TestCase):
    def test_name(self):
        self.assertEqual(op_system.OpSystem.get_name(), "Microsoft")

    def test_versia(self):
        self.assertEqual(op_system.OpSystem.get_versia(), "21H2 (10.0.22000.348) (November 22, 2021)")

    def test_relis(self):
        self.assertEqual(op_system.OpSystem.get_reliz(), "21H2")


if __name__ == '__main__':
    unittest.main()
