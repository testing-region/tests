def backspaceCompare(s, t):
    val1 = list(s)
    while '#' in val1:
        num = val1.index('#')
        if len(val1) == 2 and num == 0:
            val1.pop(num)
        elif num == 0:
            val1.pop(num)
        else:
            val1.pop(num), val1.pop(num-1)

    val2 = list(t)
    while '#' in val2:
        num = val2.index('#')
        if len(val2) == 2 and num == 0:
            val2.pop(num)
        elif num == 0:
            val2.pop(num)
        else:
            val2.pop(num), val2.pop(num-1)
    
    return val1 == val2
