# Display message about program
print("Welcome to Gross Pay Checker")
print("-"*30)

def computepay(hours, rate):
    """compute the pay for the given hours and rate"""
    # Check for extra hours and add compensation of 1.5*rate when hours > 40
    if hours < 40:
        gross_pay = hours * rate
    else:
        extra_hours = hours - 40
        gross_pay = (40 * rate) + (1.5 * rate * extra_hours)
    return gross_pay

hours = 45
rate = 10
gross_pay = computepay(hours, rate)

# Output message
print(f"After working {hours} hours, your gross pay is {gross_pay} cedis")
print("We value your service")