def hackerCards(collection, d):
    lst = []
    for i in range(1, len(collection)+2):
        print(i)
        if i > d:
            break
        elif i not in collection:
            d -= i
            lst.append(i)
    
    return lst


# test
print(hackerCards([1,2,3,4], 5))