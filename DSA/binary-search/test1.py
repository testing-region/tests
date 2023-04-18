arr = [i for i in range(1024)]

start = 0
stop = len(arr) - 1


def binary_search(arr, target, start, stop):

    # get the mid index of the start and stop indices in the
    # array to avoid slicing the array.

    # no slicing prevents wrong indices from being returned if
    # the target number is present in the array.
    mid_index = (start+stop) // 2

    if arr[mid_index] == target:
        return mid_index

    # if the end of the binary search is reached, the start and
    # stop values will be the same, hence stop the recursive call.
    if start == stop:
        return "Number not present in array"

    if arr[mid_index] > target:
        return binary_search(arr, target, start, mid_index - 1)
    else:
        return binary_search(arr, target, mid_index + 1, stop)


# Testing functions
print(binary_search(arr, -8, start, stop))
print(binary_search(arr, 8, start, stop))
