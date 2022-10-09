# PART 1

def Fahrenheit():
    # F = 32 + (C* (9/5))
    print("{0:^10}{1:^10}".format("Celsius", "Fahrenheit"))
    for C in range(101):
        F = 32 + ((9/5) * C)
        print("{0:^10}{1:^10}".format(C, round(F, 1))) 

# Fahrenheit()


# PART 2
integersList = []

while True:
    x = int(input("Enter an integer:  "))
    if x != 0:
        integersList.append(x)
    else:
        break

integersList.sort()

for integer in integersList:
    print(integer)


hoursWorked=input("enter the number of hours you worked for: ")
hourlyPay = input ("Enter the hourly pay: ")

if hoursWorked > 40:
    extraHours = hoursWorked - 40
    overtimeSalary = extraHours * (1.5 * hourlyPay )
    normalPay = 40 * hourlyPay
    grossPay = normalPay + overtimeSalary
    overtimeTaxes = 0.015 * overtimeSalary
    normalTaxes = 0.1 * normalPay
    netPay = (grossPay - normalTaxes) + (overtimeSalary - overtimeTaxes)
    print("Your gross pay is", grossPay)
    print("Your normal taxes:", normalTaxes)
    print("Your overtime taxes:", overtimeTaxes)
    print("Your net pay is", netPay)
else:
    grossPay = hoursWorked * hourlyPay
    normalTaxes = 0.1 * grossPay
    netPay = grossPay - normalTaxes
    print("Your gross pay is", grossPay)
    print("Your taxes:", normalTaxes)
    print("Your net pay:", netPay)

