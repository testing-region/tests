import random

mylist = []

for i in range(100000):
    mylist.append(random.randint(0, 100))

mylist.sort()
