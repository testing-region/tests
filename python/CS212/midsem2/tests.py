import unittest
from David_Saah import GCD


class TestMidsem2(unittest.TestCase):

    def test_GCD_1(self):
        self.assertEqual(2, GCD(34, 12))
    
    def test_GCD_2(self):
        self.assertEqual(8, GCD(64, 8))


if __name__ == '__main__':
    unittest.main()

    