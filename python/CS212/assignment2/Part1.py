##############
# Q1
##############

def min_index(num_list):
    """Returns the index of the smallest value in a list.

    Args:
        num_list (int): A list of integers.

    Returns:
        int: index of the smallest number in given list.
    """
    # To compare the values, set the smallest number to the first element
    min_num = num_list[0]
    index = -1

    for num_index in range(1, len(num_list)):
        value = num_list[num_index]
        if value > min_num:
            continue
        else:
            min_num = value
            index = num_index

    return index


##############
# Q2
##############

def max_index(num_list):
    """Returns the index of the largest value in a list.

    Args:
        num_list (int): A list of integers.

    Returns:
        int: index of the largest value in given list.
    """
    # To compare the values, set the largest number to the first element
    max_num = num_list[0]
    index = -1

    for num_index in range(1, len(num_list)):
        value = num_list[num_index]
        if value < max_num:
            continue
        else:
            max_num = value
            index = num_index

    return index


##############
# Q3
##############

def smaller_indices(list_1, list_2):
    """Returns a new list containing all indices for which the value in the first list is smaller than the value in the second list.

    Args:
        list_1 (list[int]): First list of integers.
        list_2 (list[int]): Second list of integers.

    Returns:
        list[int]: A list containing indices where value of first list < value of second list.
    """
    index_list = []

    for num_index in range(len(list_1)):
        if list_1[num_index] < list_2[num_index]:
            index_list.append(num_index)

    return index_list


##############
# Q4
##############

def pairwise_product(list_1, list_2):
    """Returns a list containing the product of values from two lists.

    Args:
        list_1 (list[int]): First list of numbers.
        list_2 (list[int]): Second list of numbers.

    Returns:
        list[int]: product of corresponding values in the first and second list of numbers.
    """
    product_list = []

    for index in range(len(list_2)):
        product_list.append(list_1[index] * list_2[index])

    return product_list


##############
# Q5
##############

def pairwise_ratio(list_1, list_2):
    """Returns a list containing the ratio of a pair of values from two lists.

    Args:
        list_1 (list[int]): First list of numbers.
        list_2 (list[int]): Second list of numbers.

    Returns:
        list[float]: ratio of corresponding values in the first and second list of numbers.
    """
    ratio_list = []

    for index in range(len(list_2)):
        ratio = round(list_1[index] / list_2[index], 3)
        ratio_list.append(ratio)

    return ratio_list
