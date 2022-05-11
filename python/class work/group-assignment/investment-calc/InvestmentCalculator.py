"""
Calculate the simple or compound interest of a user
"""

# Display information about the program
print("Welcome To Simple and Compound Interest Calculator")
print("Check the amount you will receive after finding the interest")
print("\n")

# Get input from the user
P = int(input("How much are you depositing: "))
i = int(input("What is the interest rate: "))
t = int(input("How many years are you investing this money: "))

# ask the user to choose the type of interest
interest = input("Do you want *simple* or *compound* interest: ")

# convert interest rate to percentage
r = i/100

print("\n")

# check if interest type is simple or compound
# use A = P(1 + r * t) if it is simple interest
# use A = P(1 + r) ^ t if it is compound interest
if interest == "simple":
    A = P * (1 + r*t)
    print("The amount you'll receive is", round(A, 2))
elif interest == "compound":
    A = P * ((1 + r) ** t)
    print("The amount you'll receive is", round(A, 2))
else:
    # Display an error message when the interest type is invalid
    print("[!] Not applicable, choose *simple* or *compound* interest.")
    print("Try again")