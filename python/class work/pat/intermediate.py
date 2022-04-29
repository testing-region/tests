# Write a program that does the following
# Ask the user the temperature unit they want to convert from
# Ask for the temperature unit they want to convert to
# Ask for the temperature value to be converted
# print out the converted temperature
# (NB: Your program should support converting to/from celsius, fahrenheit and kelvin)

temperature_unit = input("Enter the temperature unit you want to convert from: ")
temperature_unit_to = input("Enter the temperature unit you want to convert to: ")
temperature_value = float(input("Enter the temperature value to be converted: "))


if temperature_unit == 'celsius' and temperature_unit_to == 'fahrenheit':
    # convert from celsius to fahrenheit
    fahrenheit = (temperature_value * 9/5) + 32
    print("Your temperature in farenheit is", fahrenheit)
elif temperature_unit == 'celsius' and temperature_unit_to == 'kelvin':
    # convert from celsius to kelvin
    kelvin = temperature_value + 273.15
    print("Your temperature in kelvin is", kelvin)
elif temperature_unit == 'fahrenheit' and temperature_unit_to == 'celsius':
    # convert from fahrenheit to celsius
    celsius = (temperature_value - 32) * 5/9
    print("Your temperature in celsius is", celsius)
elif temperature_unit == 'fahrenheit' and temperature_unit_to == 'kelvin':
    # convert from fahrenheit to kelvin
    kelvin = (temperature_value - 32) * 5/9 + 273.15
    print("Your temperature in kelvin is", kelvin)
elif temperature_unit == 'kelvin' and temperature_unit_to == 'celsius':
    # convert from kelvin to celsius
    celsius = temperature_value - 273.15
    print("Your temperature in celsius is", celsius)
elif temperature_unit == 'kelvin' and temperature_unit_to == 'fahrenheit':
    # convert from kelvin to fahrenheit
    fahrenheit = (temperature_value - 273.15) * 9/5 + 32
    print("Your temperature in fahrenheit is", fahrenheit)
elif temperature_unit == 'celsius' and temperature_unit_to == 'celsius':
    # convert from celsius to celsius
    print("Your temperature in celsius is", temperature_value)
elif temperature_unit == 'fahrenheit' and temperature_unit_to == 'fahrenheit':
    # convert from fahrenheit to fahrenheit
    print("Your temperature in fahrenheit is", temperature_value)
elif temperature_unit == 'kelvin' and temperature_unit_to == 'kelvin':
    # convert from kelvin to kelvin
    print("Your temperature in kelvin is", temperature_value)
else:
    print("Invalid input")