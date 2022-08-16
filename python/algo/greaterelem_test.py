from greaterelem import solution
import unittest

class GreaterelemTest(unittest.TestCase):

    def test_no_next_greater_elem(self):
        self.assertEqual([-1, -1], solution([0, 2], [2, 0, -1]))

    def test_one_greater_elem_one_less_elem(self):
        self.assertEqual([1, -1], solution([0, 2], [2, 0, 1]))

    def test_rand_elem(self):
        self.assertEqual([3, -1], solution([2, 4], [1, 2, 3, 4]))



if __name__ == '__main__':
    unittest.main()
