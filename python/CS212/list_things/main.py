some = {
0: 0,
1: 0,
2: 0,
4: 0,
5: 0,
6: 0,
7: 0,
8: 0,
9: 0,
}

pi = '3.141592653589793'

for value in pi:
    if value == '.':
        continue
    elif int(value) in some.keys():
        some[int(value)] += 1

print(some)
