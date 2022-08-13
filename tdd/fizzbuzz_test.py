from fizzbuzz import FizzBuzz
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_return_num_for_int(self):
        self.assertEqual(2, FizzBuzz().fizzbuzz(2))

    def test_return_fizz_for_3(self):
        self.assertEqual("Fizz", FizzBuzz().fizzbuzz(3))

    def test_return_buzz_for_5(self):
        self.assertEqual("Buzz", FizzBuzz().fizzbuzz(5))



if __name__ == '__main__':
    unittest.main()
