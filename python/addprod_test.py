from addprod import Solution
import unittest

class TestAddProd(unittest.TestCase):

    def test_1(self):
        self.assertEqual(15, Solution().subtractProductAndSum(234))

    def test_2(self):
        self.assertEqual(21, Solution().subtractProductAndSum(4421))

if __name__ == '__main__':
    unittest.main()
