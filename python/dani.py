# TAKE THE INPUT OF 4 NUMBERS AND OUTPUT THE  SUM

nums = []

for x in range(4):
	a = int(input("Enter a number: "))
	nums.append(a)

sum = 0

# Adding the numbers
for i in nums:
    sum += i

print(f"The sum is {sum}")

