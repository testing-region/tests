"""Enter a number to see its factorial"""

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

a = int(input("Enter a number:  "))
if a < 0:
	raise ("ValueError: There is no value for negative numbers")
s = 1
for x in range (1, a+1):
	if a == 1 | a == 0:
		print("The answer is ", 1)
	s =  x * s
print ("The answer is ", s)