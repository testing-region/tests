import random

mylist = []

for i in range(10000):
    mylist.append(random.randint(0, 100))


def bubble_sort(items):
    n = len(items) - 1
    for i in range(n):
        for j in range(n-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

bubble_sort(mylist)
