def factorial(num):
    if num == 0 or num == 1:
        return 1
    print(num)
    return num * factorial(num-1)

def do_n(func, n):
    for i in range(n):
        func(5)

do_n(factorial, 2)
