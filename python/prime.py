a = int(input("Enter a number: "))
c = 0

for x in range(1,a):
    if a%x == 0:
        c+=1

if c == 1:
    print(a,"is a prime number\n")
else:
    print(a,"is not a prime number\n")