"""
Write a program that uses repetition and if statements to print the seven days of
a week based on the input from the user. Your program should request a number
from the user and print the day in words accordingly. Assuming the first day of
the week is Monday, the program should print Wednesday when the user enters
number 3
"""

# Display message about program
print("This program displays the day of the week that corresponds to the number you enter")
print("[!] The first day of the week is Monday")
print("-"*30)


# Get input from user
number = input("Enter a number: ")


# Check and convert to an integer
try:
    number = int(number)
except:
    print("[!] Please enter a number, try again")
    exit(1)     # exit the code after error message


# Check to display day according to number
# Monday = 1 in that order
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("[!] Number is out of range")
