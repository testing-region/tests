from shape import area_circle
from shape import circumference_circle
from shape import area_trapezoid
from shape import perimeter_trapezoid
from shape import area_cylinder
from shape import volume_cylinder
from shape import area_sphere
from shape import volume_sphere
from shape import area_cube
from shape import volume_cube

area = area_circle(5)
print("The area of a circle: ", area)

circumference = circumference_circle(4)
print("The circumference of a cirlce : ", circumference)

area = area_trapezoid(2, 4, 7)
print("The area of a trapezoid: ", area)

perimeter = perimeter_trapezoid(3, 4, 7, 3)
print("The perimeter of the trapezoid: ", perimeter)

area = area_cylinder(7, 6)
print("The area of the cylinder: ", area)

volume = volume_cylinder(5,6 )
print("The volume of the cylinder: ", volume)

area = area_sphere(7)
print("The area of the sphere: ", area)

volume = volume_sphere(6)
print("The volume of the sphere: ", volume)

area = area_cube(6)
print("The area of the cube: ", area)

volume = volume_cube(5)
print("The volume of the cube:", volume)