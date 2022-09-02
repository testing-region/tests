import math

# Function for area of a circle
def area_circle(radius):
    area = math.pi * radius**2
    return round(area, 2)
    

# Function for circumference of a circle 
def circumference_circle(radius):
    circumference = 2 * math.pi * radius
    return round(circumference, 2)

# Function for area of a trapezoid
def area_trapezoid(base_1, base_2, height ):
    area = 1/2 * (base_1 + base_2) * height
    return round(area, 2)

# Function for perimeter of a trapezoid 
def perimeter_trapezoid(side_1, side_2, side_3, side_4):
    perimeter = side_1 + side_2 + side_3 + side_4
    return round(perimeter, 2)

# Function for area of a cylinder
def area_cylinder(radius, height):
    area = (2 * math.pi * height * radius) + (2 * math.pi * radius**2)
    return round(area, 2)

# Function for volume of a cylinder 
def volume_cylinder(radius, height):
    volume = math.pi * radius **2 * height
    return round(volume, 2)

# Function for area of a sphere
def area_sphere(radius):
    area = 4 * math.pi * radius **2
    return round(area, 2)

# Function for volume of a sphere
def volume_sphere(radius):
    volume = 4/3 * math.pi * radius ** 3
    return round(volume, 2)

# Function for area of a curebe 
def area_cube(sides):
    area = 6 * sides**2
    return round(area, 2)

# Function for volume of a cube - Question 5(I chose a cube)
def volume_cube(sides):
    volume = sides**3
    return round(volume, 2)
