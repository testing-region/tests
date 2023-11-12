# PART 1
# q1
def min_index(lst):
    """
    Returns the index of the smallest value in the list

    Parameters
    -----------
    lst
        list: a given list

    Returns
    --------
    returns index of smallest value
    """
    small = min(lst)
    num = lst.index(small)
    return num


lst = [40, 50, 10, 90, 100, 70]
print("min_index:", min_index(lst))


# q2
def max_index(lst):
    big = max(lst)
    num = lst.index(big)
    return num


lst = [40, 50, 10, 90, 100, 70]
print("max_index:", max_index(lst))


# q3
def smaller_indices(lst1, lst2):
    new_lst = []
    for i, j in zip(lst1, lst2):
        if i < j:
            num = lst1.index(i)
            new_lst.append(num)

    return new_lst


lst1 = [40, 50, 10, 90, 100, 70]
lst2 = [60, 20, 19, 95, 30, 20]
print("smaller_indices:", smaller_indices(lst1, lst2))


# q4
def pairwise_product(lst1, lst2):
    empty_lst = []
    for i, j in zip(lst1, lst2):
        num = i * j
        empty_lst.append(num)

    return empty_lst


lst1 = [40, 50, 10, 90]
lst2 = [6, 2, 2, 5]
print("pairwise_product:", pairwise_product(lst1, lst2))


# q5
def pairwise_ratio(lst1, lst2):
    empty_lst = []
    for i, j in zip(lst1, lst2):
        num = i / j
        num = round(num, 3)
        empty_lst.append(num)

    return empty_lst


lst1 = [40, 50, 10, 90, 100, 70]
lst2 = [60, 20, 19, 95, 30, 20]
print("pairwise_ratio:", pairwise_ratio(lst1, lst2))
