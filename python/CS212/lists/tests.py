import unittest
import Part2
import Part3
import Part4


class TestActivity(unittest.TestCase):

    def test_Part2(self):
        self.assertEqual([76, 92.3, 'hello', True, 4, 76], Part2.my_list)

    def test_Part3(self):
        self.assertEqual([99, 92.3, 'cat', 'hello', 4, 76, 'apple', 76], Part3.my_list)

    def test_Part4(self):
        self.assertEqual(29, Part4.sum_of_sqaures([2,3,4]))

    def test_Part4_2(self):
        self.assertEqual(4900, Part4.sum_of_sqaures(list(range(1, 25))))
    

if __name__ == '__main__':
    unittest.main()