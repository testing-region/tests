import unittest
from twosum import twoSum

class TestTwoSum(unittest.TestCase):

    def test1(self):
        self.assertEqual([0, 1], twoSum([2, 7, 11, 15], 9))

    def test2(self):
        self.assertEqual([1, 2], twoSum([3, 2, 4], 6))

    def test3(self):
        self.assertEqual([0, 1], twoSum([3, 3], 6))

    def test4(self):
        self.assertEqual([2, 4], twoSum([-1,-2,-3,-4,-5], -8))

if __name__ == '__main__':
    unittest.main()
