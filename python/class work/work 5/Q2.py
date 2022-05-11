"""
Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and  rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
Note that 475 = 40 * 10 + 5 * 15
"""


# Display message about program
print("Welcome to Gross Pay Checker")
print("[!] Enter the number of hours worked and the rate charged(in cedis) per hour")
print("-"*30)

# Get input from user
hours = float(input("Enter the hours worked: "))
rate = float(input("Enter the hourly rate: "))

def computepay(hours, rate):
    """compute the pay for the given hours and rate"""
    # Check for extra hours and add compensation of 1.5*rate when hours > 40
    if hours < 40:
        gross_pay = hours * rate
    else:
        extra_hours = hours - 40
        gross_pay = (40 * rate) + (1.5 * rate * extra_hours)
    return gross_pay

gross_pay = computepay(hours, rate)

# Output message
print("\n")
print(f"After working {hours} hours, your gross pay is {gross_pay} cedis")
print("We value your service")