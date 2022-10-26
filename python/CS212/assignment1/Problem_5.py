age_in_months = int(input("How many months old is your child?: "))

# There are 12 months in a year
# The number of 12 months in age_in_months = number of years
# remaining months = number of months (after calculating years)

age_in_years = age_in_months // 12
remaining_months = age_in_months % 12

# add new line for readable output
print("")

print("Your child is", age_in_years, "year(s),", remaining_months, "month(s) old.")
