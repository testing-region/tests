import random


def merge(left_arr, right_arr):
    left_index = 0
    right_index = 0
    sorted_arr = []

    while (left_index < len(left_arr)) and (right_index < len(right_arr)):
        if left_arr[left_index] < right_arr[right_index]:
            sorted_arr.append(left_arr[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_arr[right_index])
            right_index += 1

    return sorted_arr + left_arr[left_index:] + right_arr[right_index:]


def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid_index = len(arr) // 2
    left_arr = arr[0:mid_index]
    right_arr = arr[mid_index:]

    return merge(mergesort(left_arr), mergesort(right_arr))


arr = [random.randint(1, 100) for i in range(100)]
#print(arr)
print(mergesort(arr))
