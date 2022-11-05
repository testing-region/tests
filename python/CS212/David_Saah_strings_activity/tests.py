import Part1
import Part2
import Part3
import unittest


class TestStringActivity(unittest.TestCase):

    def test_part1_1(self):
        self.assertEqual(True, Part1.is_vowel("e"))

    def test_part1_2(self):
        self.assertEqual(False, Part1.is_vowel("p"))

    def test_part2_1(self):
        self.assertEqual(1, Part2.first_vowel_index("some"))

    def test_part2_2(self):
        self.assertEqual(-1, Part2.first_vowel_index("hymn"))

    def test_part3_1(self):
        self.assertEqual("oosechay", Part3.english_to_piglatin("choose"))

    def test_part3_2(self):
        self.assertEqual("oatgay", Part3.english_to_piglatin("goat"))

    def test_part3_3(self):
        self.assertEqual("elephantway", Part3.english_to_piglatin("elephant"))
    
    def test_part3_4(self):
        self.assertEqual("No pig latin translation available for words without vowels", Part3.english_to_piglatin("hymn"))



if __name__ == '__main__':
    unittest.main()