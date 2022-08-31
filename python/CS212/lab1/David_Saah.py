"""
1. The int() function taking float as an argument, converts it into an integer by returning only the whole number part.
In contrast, the round() function taking float as an argument, rounds up the number to the nearest integer.
"""

print("Confirming Behaviour of int() and round()")
print("int(3.54):", int(3.54))        # displays 3
print("round(3.54):", round(3.54))    # displays 4
print("int(3.45):", int(3.45))        # displays 3
print("round(3.45):", round(3.45))    # displays 3
print("")

# --------------------------------------------------------------------------------

import math


def display_cone_surface_area(radius, slant_length):
    # calculate surface area using radius and slant length
    area = (math.pi * radius**2) + (math.pi * radius * slant_length)
    print("The surface area of the cone is", round(area, 2))

def display_cone_volume(radius, height):
    # calculate volume using radius and height
    volume = (1/3) * math.pi * radius**2 * height
    print("The volume of the cone is", round(volume, 2))

# --------------------------------------------------------------------------------

# Tests for area
print("Testing for surface area: using radius & slant length")
display_cone_surface_area(2, 4)         # answer = 37.7
display_cone_surface_area(3, 37.7)      # answer = 383.59
print("")

# Tests for volume
print("Testing for volume: using radius & height")
display_cone_volume(2, 4)           # answer = 16.76
display_cone_volume(37.7, 4.8)      # answer = 7144.18