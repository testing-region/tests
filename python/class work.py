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
nintendo_price = 249.99

# Find the difference of the amount
difference = math.modf(user_money/nintendo_price)

# Set the number of nintendo and the remainder of the money
number_of_nintendo = int(difference[1])
money_left = difference[0]

# Set money needed to buy a nintendo wii
amount_needed = nintendo_price - money_left
# Round to 2 decimal places
amount_needed = round(amount_needed, 2)

# Check if money is sufficient or not
if user_money > nintendo_price:
    print("You can buy", number_of_nintendo, "Nintendo Wiis")
    print("You need", amount_needed, "dollars to buy an extra one")
else:
    amount_required = nintendo_price - user_money
    print("You don't have enough money to buy a Nintendo Wii")
    print("You need", amount_required, "dollars more.")






