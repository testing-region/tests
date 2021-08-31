a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))
c = int(input("Enter the value c: "))

sqrtVal = b**2 - (4*a*c)
x1 = (-b + sqrtVal**0.5)/2*a
x2 = (-b - sqrtVal**0.5)/2*a

if sqrtVal < 0:
    print("No real roots!")
else:
    if x1 == x2:
        print(f"The root of the equation is: {x1}")
    else:
        print(f"The roots of the equation are: {x1} and {x2}")

