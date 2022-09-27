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

start = 0
stop = len(arr) - 1

def binary_search(arr, target, start, stop):
    mid_index = math.floor((start+stop)/2)
    
    if arr[mid_index] == target:
        return mid_index
    elif len(arr[start:stop]) == 0:
        return "Number not present in array"
    
    if arr[mid_index] > target:
        return binary_search(arr, target, start, mid_index - 1)
    else:
        return binary_search(arr, target, mid_index + 1, stop)


print(binary_search(arr, 8, start, stop))
