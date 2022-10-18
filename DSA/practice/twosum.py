def twoSum(nums: list[int], target: int) -> list[int]:
    result = []
    new = []

    for i in range(len(nums)):
        if nums[i] > target:
            continue
        else:
            new.append(nums[i])

    high = max(new)
    high_index = nums.index(high)
    result.append(high_index)
    low = target - high
    
    if new.count(high) > 1:
        result.append(nums.index(low, high_index+1))
    else:
        result.append(nums.index(low))

    result.sort()
    return result
