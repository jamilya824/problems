from problem6 import result
import unittest


class Test(unittest.TestCase):
    def test_result(self):
        self.assertEqual(result, 25164150)


if __name__ == '__main__':
    unittest.main()
