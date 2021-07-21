"""Enter a year to see calendar"""

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

import calendar as c
print ("Welcome to MyCalender\nEnter a year to see dates\n")
try:
	df1 = input("Year: ")
	df = int(df1)
except:
	print("Invalid input, try again!")
	df1 = input("Year: ")
	df = int(df1)
	
print (c.calendar(df))
