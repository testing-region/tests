"""
Write a program that convert a temperature entered in degrees Fahrenheit
to degrees Celcius. Your program on execution, should contain a program
description and program greeting.
"""

# Display Information
print("\n")
print("Welcome To Temperature Convertor")
print("-"*50)
print("[!] Enter a temperature value in degrees Fahrenheit(°F) to see its value in degrees Celcius(°C)\n")

# Take input from user
deg_fahrenheit = float(input("Enter the temperature (in degrees Fahrenheit): "))

# Formula for conversion
# (32°F − 32) × 5/9 = 0°C

# calculate for degrees celcius
deg_celcuis = (deg_fahrenheit - 32) * (5/9)

# Display conversion message
print("\n")
print("="*50)
print("{:^50}".format(f"{deg_fahrenheit}°F is {round(deg_celcuis, 2)}°C"))
print("="*50)
print("\n")