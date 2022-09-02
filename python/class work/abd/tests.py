#!/usr/bin/env python

import unittest
import shape
import math


class TestShapes(unittest.TestCase):
    
    def testCircleArea(self):
        self.assertEqual(12.57, shape.area_circle(2))

    def testCircumferenceCircle(self):
        self.assertEqual(18.85, shape.circumference_circle(3))

    def testAreaTrapezoid(self):
        self.assertEqual(52.5, shape.area_trapezoid(23, 12, 3))

    def testPerimeterTrapezoid(self):
        self.assertEqual(145, shape.perimeter_trapezoid(23, 43, 12, 67))

    def testAreaCylinder(self):
        self.assertEqual(1206.37, shape.area_cylinder(12, 4))

    def testVolumeCylinder(self):
        self.assertEqual(75.4, shape.volume_cylinder(2, 6))

    def testAreaSphere(self):
        self.assertEqual(113.1, shape.area_sphere(3))

    def testVolumeSphere(self):
        self.assertEqual(268.08, shape.volume_sphere(4))

    def testAreaCube(self):
        self.assertEqual(54, shape.area_cube(3))

    def testVolumeCube(self):
        self.assertEqual(1728, shape.volume_cube(12))


if __name__ == '__main__':
    unittest.main()
