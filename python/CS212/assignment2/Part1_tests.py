import unittest
import Part1


class TestPart1(unittest.TestCase):

    def test_min_index_1(self):
        self.assertEqual(2, Part1.min_index([40, 50, 10, 90, 100, 70]))

    def test_min_index_2(self):
        self.assertEqual(2, Part1.min_index([60, 20, 19, 95, 30, 20]))

    def test_max_index_1(self):
        self.assertEqual(4, Part1.max_index([40, 50, 10, 90, 100, 70]))

    def test_max_index_2(self):
        self.assertEqual(3, Part1.max_index([60, 20, 19, 95, 30, 20]))

    def test_smaller_indices_1(self):
        self.assertEqual(
            [0, 2, 3],
            Part1.smaller_indices(
                [40, 50, 10, 90, 100, 70], [60, 20, 19, 95, 30, 20]
            )
        )

    def test_smaller_indices_2(self):
        self.assertEqual(
            [1, 4, 5],
            Part1.smaller_indices(
                [60, 20, 19, 95, 30, 20], [40, 50, 10, 90, 100, 70]
            )
        )

    def test_pairwise_product_1(self):
        self.assertEqual(
            [240, 100, 20, 450],
            Part1.pairwise_product([40, 50, 10, 90], [6, 2, 2, 5])
        )

    def test_pairwise_product_2(self):
        self.assertEqual(
            [80, 100, 20, 180, 200, 140],
            Part1.pairwise_product(
                [40, 50, 10, 90, 100, 70], [2, 2, 2, 2, 2, 2])
        )

    def test_pairwise_ratio_1(self):
        self.assertEqual(
            [0.667, 2.5, 0.526, 0.947],
            Part1.pairwise_ratio(
                [40, 50, 10, 90], [60, 20, 19, 95])
        )

    def test_pairwise_ratio_2(self):
        self.assertEqual(
            [20.0, 25.0, 5.0, 45.0, 50.0, 35.0],
            Part1.pairwise_ratio(
                [40, 50, 10, 90, 100, 70], [2, 2, 2, 2, 2, 2])
        )


if __name__ == '__main__':
    unittest.main()
