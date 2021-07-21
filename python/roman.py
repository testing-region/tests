'''
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:
solution('XXI') # should return 21
'''

'''
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000


The value of a roman numeral sequence is calculated by simply adding together the numerals, from left to right.
Writing numerals that decrease from left to right represents addition of the numbers. For example, LX represents 50 + 10 = 60 and XVI represents 10 + 5 + 1 = 16.

    IV = 5 - 1
    IX = 10 - 1
    XL = 50 - 10
    XC = 100 - 10
    CD = 500 - 100
    CM = 1000 - 10

For example, the number 1988 converted to roman numerals is MCMLXXXVIII which is calculated from left-to-right as:
M+CM+L+X+X+X+V+I+I+I
'''


def roman(x):
    value = {
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
    }
    data = [i for i in x.split()]
    data1 = []
    for num in data:
        data1.append(value[num])
    sum = 0
    for y in data1:
        sum += y
    return sum


print(roman('XXI'))


