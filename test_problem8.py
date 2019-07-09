from problem8 import max_product
import unittest


class Test(unittest.TestCase):
    def test_result(self):
        self.assertEqual(max_product(), 23514624000)


if __name__ == '__main__':
    unittest.main()
