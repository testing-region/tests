import math


"""
PART 1: What is the output?

# Level 1
Babatunde

# Level 2
Babatunde

# Level 3
Babatunde
None

# Level 4
Babatunde
35

# Level 5
Babatunde
35

# Level 6
Babatunde
None
35
None

# Level 7
No output

# level 8
No output

# Level 9
Babatunde

# Level 10
No output

# Level 11
No output

# Level 12
No output

# Level 13
Darren
37

# Level 14
Darren
None
37

END OF PART 1
"""


"""
PART 2: Writing code
"""

# Level 1
def say_hello(name):
    print("Hello,", name)


# Level 2
def area_of_room(width, length):
    area = length * width
    print("The area of the room is", round(area, 4), "squared units")


# Level 3
def area_of_field(width, length):
    area_in_feet = width * length
    
    # 1 acre = 43,560 sq. ft. 
    area_in_acres = area_in_feet / 43560
    print("The area of the farmer's field is", round(area_in_acres, 4), "acres")


# Level 4
def sum_of_integers(n):
    sum_to_n = (n * (n + 1)) / 2
    print("The sum of numbers from 1 to n is:", sum_to_n)


# Level 5
def total_price_day_old_bread(num_of_loaves):
    fresh_bread_unit_price = 10
    discount = 55/100
    day_old_bread_unit_price = fresh_bread_unit_price - (fresh_bread_unit_price * discount)
    total_price = day_old_bread_unit_price * num_of_loaves
    print(num_of_loaves, "loaves of day-old bread costs GHC", round(total_price, 2))


# Level 6
def convert_temp_to_kelvin_and_celcius(temperature):
    # F = (C * 9/5) + 32
    fahrenheit = (temperature * (9/5)) + 32
    
    # K = C + 273.15
    kelvin = temperature + 273.15

    print(temperature, "degrees Celcius is", fahrenheit, "degrees Fahrenheit")
    print(temperature, "degrees Celcius is", kelvin, "degrees Kelvin")


# Level 7
def area_of_triangle(length, height):
    area = (1/2) * length * height
    print("The area of the triangle is", area, "metres squared")


# Level 8
def display_amount_of_gas(pressure, volume, temperature):
    # PV = nRT
    # n =PV/RT
    R = 8.314
    amount_of_gas = (pressure * volume) / (R * temperature)
    print("The amount of gas contained is", round(amount_of_gas, 4), "moles")


# Level 9
def volume_of_cylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    print("The volume of the cylinder is", round(volume, 1), "metres cubed")


"""
Calling functions
"""

say_hello("David Saah")
area_of_room(200, 200)
area_of_field(200, 200)
sum_of_integers(10)
total_price_day_old_bread(20)
convert_temp_to_kelvin_and_celcius(25)
area_of_triangle(10, 25)
display_amount_of_gas(10, 25, 200)
volume_of_cylinder(12, 46)
