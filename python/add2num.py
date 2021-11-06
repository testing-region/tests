def addTwoNumbers(l1, l2):
    r_l1, r_l2 = l1[::-1], l2[::-1]
    new_l1 = new_l2 = ''
    
    for i in r_l1:
        new_l1 += str(i)
    for j in r_l2:
        new_l2 += str(j)

    total = int(new_l1) + int(new_l2)
    new_val = [i for i in str(total)]
    
    return new_val[::-1]


print(addTwoNumbers([2,4,3], [5,6,4]))
