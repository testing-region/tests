from array123 import array123
import unittest

class TestArray123(unittest.TestCase):

    def test_1(self):
        self.assertEqual(True, array123([1, 1, 2, 3, 1]))

    def test_2(self):
        self.assertEqual(False, array123([1, 1, 2, 4, 1]))
    
    def test_3(self):
        self.assertEqual(True, array123([1, 1, 2, 1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
