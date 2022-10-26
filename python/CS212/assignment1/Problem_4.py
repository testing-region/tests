import math

# shape of tank = cylinder
# volume of water = volume of cylinder formed by water
# volume = pi * r^2 * h

height = float(input("What is the height of your polytank: "))
radius = float(input("What is the radius of your polytank: "))

volume = math.pi * (radius ** 2) * height

# add new line for readable output
print("")

print("You can order", round(volume, 2), "meter cubed of water for your polytank to be full.")
