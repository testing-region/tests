import math


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
def linear_search(arr, num):
    for i in len(arr):
        if num = arr[i]:
            return i
    else:
        return "Element not present in array"
'''

def binary_search(arr, num):
    mid = math.floor(len(arr)/2)
    
    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        arr = arr[:mid-1]
    elif arr[mid] < num:
        arr = arr[mid-1:]
    else:
        return "Element not present in array"
    
    return binary_search(arr, num)


print(binary_search(arr, 8))
