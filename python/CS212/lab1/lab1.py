import math


def display_cone_area(radius, slant_length):
    area = (math.pi * radius**2) + (math.pi * radius * slant_length)
    return round(area, 2)


def display_cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return round(volume, 2)

