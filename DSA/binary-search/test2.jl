arr = [i for i in 1:1024]

start = 1
stop = length(arr)

function binary_search(arr, target, start, stop)
    mid_index = convert(Int64, floor((start+stop) / 2))

    if arr[mid_index] == target
	return mid_index
    elseif start == stop
	return "Number not present in array"
    end

    if arr[mid_index] > target
	return binary_search(arr, target, start, mid_index - 1)
    else
	return binary_search(arr, target, mid_index += 1, stop)
    end

end


# Testing functions
println(binary_search(arr, -8, start, stop))
println(binary_search(arr, 8, start, stop))
