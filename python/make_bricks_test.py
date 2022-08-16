from make_bricks import make_bricks
import unittest

class MakeBricksTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(True, make_bricks(3, 1, 8))

    def test_2(self):
        self.assertEqual(False, make_bricks(3, 1, 9))
    
    def test_3(self):
        self.assertEqual(True, make_bricks(3, 2, 10))

    def test_4(self):
        self.assertEqual(False, make_bricks(3, 2, 9))


if __name__ == '__main__':
    unittest.main()
