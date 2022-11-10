################
# Q5
################

def GCD(a, b):
    """returns the greatest common divisor of two numbers

    Args:
        a (int): positive integer
        b (int): positive integer

    Returns:
        int: greatest common divisor of a and b, (-1 if a or b are not positive integers)
    """

    # check if a and b are positive integers
    if (not isinstance(a, int) or a < 0) and (not isinstance(b, int) or b < 0):
        return -1

    if b == 0:
        return a
    else:
        c = a % b
        return GCD(b, c)


print("Q5")
print("-" * 20)
print("The greatest common divisor of 34 and 12 is", GCD(34, 12))
print("The greatest common divisor of 64 and 8 is", GCD(64, 8))


################
# Q6
################
print("\nQ6")
print("-" * 20)

product = 1     # since the identity number for multiplication is 1

while True:
    num = float(input("Enter a number: "))

    if num < 0:
        print("\nThe product of the sequence of numbers is", product)
        break
    else:
        product *= num


################
# Q7
################
print("\nQ7")
print("-" * 20)

hired = False

while not hired:
    prompt = input("Are there any more candidates? [Y/N]: ")

    if prompt.upper() == "Y":
        py_proficiency = float(
            input("How proficient is the candidate in python? [1-10]: "))
        start_now = input(
            "Is the candidate willing to start immediately? [Y/N]: ")

        if py_proficiency >= 7.5 and start_now.upper() == "Y":
            hired = True
            print("\n[!] Response: Candidate qualified! Hire candidate!")
        else:
            print("\n[!] Response: Candidate not qualified!!!\n")

    elif prompt.upper() == "N":
        hired = True    # needs to evaluate to True to end the loop when no candidates are available
        print("\n[!] Response: No more candidates available for hire.")
