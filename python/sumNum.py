# accept a non-zero positive integer from user
# get the sum of all integers between 1 and the number entered

num = int(input("Enter a number: "))

sum = 0

for x in range(num+1):
    sum += x

print(sum)