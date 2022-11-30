import unittest
import Part2_Q1


class Testquestion_1(unittest.TestCase):

    # Question 1 tests
    def test_country_names_data_1(self):
        self.assertEqual("Zimbabwe", Part2_Q1.country_names[-1])

    def test_population_data(self):
        self.assertEqual(13771721, Part2_Q1.population_list[-1])

    def test_literacy_data(self):
        self.assertEqual(84, Part2_Q1.percent_literacy_rate[-1])

    def test_electricty_prod_data(self):
        self.assertEqual(46, Part2_Q1.electricity_prod_amt[0])

    def test_country_dict_type(self):
        self.assertEqual(True, isinstance(Part2_Q1.country_names_dict, dict))


if __name__ == '__main__':
    unittest.main()
