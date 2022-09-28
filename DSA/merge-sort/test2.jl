import Random


function merge(left_arr::AbstractVector, right_arr::AbstractVector)
    left_index = 1
    right_index = 1
    sorted_arr::AbstractVector{Int64} = []

    while (left_index < length(left_arr) + 1) && (right_index < length(right_arr) + 1)
	if left_arr[left_index] < right_arr[right_index]
           append!(sorted_arr, left_arr[left_index])
	    left_index += 1
	 else
	    append!(sorted_arr, right_arr[right_index])
	    right_index += 1
	end
    end
    
    return append!(sorted_arr, left_arr[left_index:length(left_arr)], right_arr[right_index:length(right_arr)])
end


function mergesort(arr::AbstractVector)
    if length(arr) == 1
	return arr
    end

    mid_index = convert(Int64, floor(length(arr) / 2))
    left_arr = arr[1:mid_index]
    right_arr = arr[mid_index+1:length(arr)]

    return merge(mergesort(left_arr), mergesort(right_arr))
end


arr = [Random.rand(1:100) for i in 1:100]
println(mergesort(arr))
