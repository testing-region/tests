"""
Next greater element
"""


def solution(nums1, nums2):
    new_list = []
    nums3 = list(nums2)
    nums3.pop(0)
    nums3.append(-1)
    nums = dict(zip(nums2, nums3))
    for x in range(len(nums1)):
        if nums1[x] < nums[nums1[x]]:
            new_list.append(nums[nums1[x]])
        else:
            new_list.append(-1)
    return new_list
