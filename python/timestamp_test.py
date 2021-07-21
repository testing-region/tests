from datetime import datetime, date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print('Current Time =' , current_time)


today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year\t\n",
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

#Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
   