"""
Write a python program that allows the user to enter any integer value 
and displays the value of 2 raised to that power. Your program should 
function as shown below:
    What power of two? 10
    Two to the power of 10 is 1024
"""

# get input from the user
power = int(input("What power of two?: "))

# raise 2 to that power
answer = 2 ** power

# output message
print("Two to the power of", power, "is", answer)
