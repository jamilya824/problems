from problem9 import result
import unittest


class Test(unittest.TestCase):
    def test_result(self):
        self.assertEqual(result, 31875000)


if __name__ == '__main__':
    unittest.main()