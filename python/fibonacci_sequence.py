"""Returns the first n Fibonacci numbers"""

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

x=1
y=0
n=int(input ("Enter the length of the sequence: "))
for i in range(n):
    y=x+y
    print(y)
    x=y-x