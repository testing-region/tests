# Use height,width and expected load as your variables

# This is a Java code... Since you use python just reuse the refactor the code
# with python
# ####Height = height*12; // needed to make height calculations in inches
# 		Area = Math.pow(width, 2);
# 		float E = modulus_of_elasticity; // one if statement to check 3 conditions
# 		If ((((height)/width)<= slenderness_limit)&&
# 		(expectedLoad <= ((0.3 * E * area)/Math.pow((height/width), 2)))&&
# 		(expectedLoad <= (area * maximum_allowable_stress))){

width = float(input("Enter the width(in meters): "))
height = float(input("Enter the height(in meters): "))
expected_load = float(input("Enter the expected(in newtons): "))
# width = 10
# height = 894  #40....10,
# expected_load = 1000000

# Declaring variables and constants
E = 1700000  # Modulus of elasticity
maximum_allowable_stress = 1450
slenderness_limit = 50
area = width ** 2
slenderness = height / width

# Test_1: Slenderness test


def slender_test():
    if slenderness <= slenderness_limit:
        print("Passed slenderness test!\n")
        return True
    else:
        print("!.Failed slenderness test")
        print("Posible solutions:\nIncrease the width\nReduce the height\n")
        return False

# slender_test()
# dependent variables
# - slenderness

# # Possible solution to test_1 fail
# 1. Increase the width
# 2. Reduce the height


# Test_2:
def test_2():
    if expected_load <= (0.3 * E * area) / slenderness ** 2:
        print("Passed second test!\n")
        return True
    else:
        print("!.Failed second test")
        print("Posible solutions:\nIncrease the width\nReduce the height\n")
        return False


# test_2()

# dependent variables
# - slenderness
# - area

# # Possible solution to test_2 fail
# 1. Increase the width
# 2. Reduce the height


# Test_3: Maximum load
def max_load():
    if expected_load <= area * maximum_allowable_stress:
        print("Passed maximum load test!\n")
        return True
    else:
        print("!.Failed maximum load test")
        print("Posible solutions:\n - Increase the width\n")
        return False

# max_load()
# dependent variables
# - width

# # Verified solution to test_2 fail
# 1. Increase the width


print("\n")
print("Checking structural intergrity...\n")
if slender_test() and test_2() and max_load():
    print("All tests have been passed, you are good to go!")
else:
    test_2()
    max_load()
