"""
Write a program to prompt the user for hours and rate per hour
to compute gross pay
"""

# Display information
print("\n")
print("Welcome To Gross Pay Checker")
print("-"*50)
print("[!] Enter the number of hours worked and the rate charged(in cedis) per hour\n")


# Take input from user
hours_worked = float(input("Enter the number of hours you worked: "))
rate_per_hour = float(input("Enter the rate per hour: "))

# Calculate the gross pay
gross_pay = hours_worked * rate_per_hour

# Display message showing gross pay
print("\n")
print(f"After working for {hours_worked} hours at a rate of {rate_per_hour} cedis per hour, your gross pay is {gross_pay} cedis.")
print("\n")