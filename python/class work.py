"""
Exercise: Write a python program that prompts the user for his/her amount of money,
then reports how many Nintendo Wii's the person can afford, and how much more money
he/she will need to afford an additional Wii.

price of nintendo = 249.99 dollars
"""

import math

# Get money from user
user_money = float(input("How much money do you have?: "))

# Set the nintendo price
nintendo_price = 250

# Find the difference of the amount
difference = math.modf(user_money/nintendo_price)

# Set the number of nintendo and the remainder of the money
number_of_nintendo = int(difference[1])
money_left = round(difference[0], 2)

# Set money needed to buy a nintendo wii
amount_needed = nintendo_price - money_left

# Check if money is sufficient or not
if user_money >= nintendo_price:
    # Display message
    print("You can buy", number_of_nintendo, "Nintendo Wiis")
    print("You need", amount_needed, "dollars to buy an extra one")
else:
    # Check for the amount required if the user's money is less than the nintendo price
    amount_required = nintendo_price - user_money
    # Display message
    print("You don't have enough money to buy a Nintendo Wii")
    print("You need", amount_required, "dollars more.")






