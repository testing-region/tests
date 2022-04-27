"""
Rewrite your pay computation to give the employee 1.5 times the hourly rate for
hours worked above 40 hours.
Sample:
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
475 = 40*10 + 5*1.5
"""

# Display message about program
print("Welcome to Gross Pay Checker")
print("[!] Enter the number of hours worked and the rate charged(in cedis) per hour")
print("-"*30)



# Get input from user
hours = input("Enter the hours worked: ")
rate = input("Enter the hourly rate: ")

# check input for errors and convert to float
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Please enter a number, try again")
    exit(1)     # exit the code after error message

# Check for extra hours and add compensation of 1.5*rate when hours > 40
if hours < 40:
    gross_pay = hours * rate
else:
    extra_hours = hours - 40
    gross_pay = (40 * rate) + (1.5 * rate * extra_hours)
    
# Output message
print("\n")
print(f"After working {hours} hours, your gross pay is {gross_pay} cedis")
print("We value your service")
