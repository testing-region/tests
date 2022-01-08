def gamerColors(val):
    w = 0
    b = 0
    for i in range(len(val)-2):
        if val[i] == val[i+1] and val[i+1] == val[i+2]:
            if val[i] == 'w':
                w += 1
            elif val[i] == 'b':
                b += 1

    # return w, b    
    if w > b:
        return 'wendy'
    else:
        return 'bob'


# test
# print(gamerColors('wwwbbbww'))
print(gamerColors('wwwbb'))