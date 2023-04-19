def twoSum(nums: list[int], target: int) -> list[int]:
    result = []
    pos_arr = []
    neg_arr = []

    for i in range(len(nums)):
        if nums[i] < target and nums[i] > 0:
            pos_arr.append(nums[i])
        elif nums[i] > target and nums[i] < 0:
            neg_arr.append(nums[i])

    if len(pos_arr) != 0:
        high = max(pos_arr)
        low = target - high
    else:
        high = min(neg_arr)
        low = target + high

    high_index = nums.index(high)
    result.append(high_index)

    if pos_arr.count(high) > 1 or neg_arr.count(high):
        result.append(nums.index(low, high_index+1))
    else:
        result.append(nums.index(low))

    result.sort()
    return result
