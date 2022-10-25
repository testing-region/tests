nums = [1,2,3,4]

for x in nums[:]:
    if x in nums:
        nums.remove(x)
    
print(nums)