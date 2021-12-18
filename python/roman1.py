# accept integer from user
# check if number is between 1 and 10 inclusive
# if number is between 1 and 10 inclusive, convert to roman numeral
# else print error message

num = int(input("Enter a number between 1 and 10: "))

roman = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: 'X'
}

if num in roman:
    print(roman[num])
else:
    print("Error: Number is not between 1 and 10")