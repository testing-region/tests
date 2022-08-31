import unittest
import lab1

class AssignmentTest(unittest.TestCase):
    
    def test_1_volume(self):
        self.assertEqual(16.76, lab1.display_cone_volume(2, 4))
        
    def test_2_area(self):
        self.assertEqual(37.7, lab1.display_cone_area(2, 4))
        
    def test_3_volume(self):
        self.assertEqual(26.59, lab1.display_cone_volume(2.3, 4.8))
        
    def test_4_area(self):
        self.assertEqual(51.3, lab1.display_cone_area(2.3, 4.8))
    
    def test_5_volume(self):
        self.assertEqual(7144.18, lab1.display_cone_volume(37.7, 4.8))
    
    def test_6_area(self):
        self.assertEqual(383.59, lab1.display_cone_area(3, 37.7))
        
if __name__ == '__main__':
    unittest.main()