# Taking inputs from the user
width = float(input("Enter the width(in meters): "))
height = float(input("Enter the height(in meters): "))
expected_load = float(input("Enter the expected(in newtons): "))


# Declaring variables and constants
E = 1700000  # Modulus of elasticity
maximum_allowable_stress = 1450
slenderness_limit = 50
area = width ** 2
slenderness = height / width


# Declaring test functions
def slender_test():
    '''Slenderness test'''
    if slenderness <= slenderness_limit:
        print("Passed slenderness test!\n")
        return True
    else:
        print("!.Failed slenderness test")
        print("Posible solutions:\n- Increase the width\n- Reduce the height\n")
        return False

def test_2():
    '''Second test'''
    if expected_load <= (0.3 * E * area) / slenderness ** 2:
        print("Passed second test!\n")
        return True
    else:
        print("!.Failed second test")
        print("Posible solutions:\n- Increase the width\n- Reduce the height\n")
        return False

def max_load():
    '''Maximum load test'''
    if expected_load <= area * maximum_allowable_stress:
        print("Passed maximum load test!\n")
        return True
    else:
        print("!.Failed maximum load test")
        print("Posible solutions:\n - Increase the width\n")
        return False


# Test analysis and outputs
print("\n")
print("Checking structural intergrity...\n")
if slender_test() and test_2() and max_load():
    print("All tests have been passed, you are good to go!")
else:
    test_2()
    max_load()

