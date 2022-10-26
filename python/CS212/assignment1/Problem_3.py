import math

radius = 2.5
height = 4

# volume of cone = 1/3 * pi * r^2 * h
# for this problem, volume of cone = sphere_volume

sphere_volume = (1/3) * math.pi * (radius ** 2) * height

print("The volume of the cone is", round(sphere_volume, 2), "cm squared.")