def twoSum(nums, target):
    mapping = {}

    for i, j in enumerate(nums):
        diff = target - j
        if diff in mapping:
            return [mapping[diff],  i]
        
        mapping[j] = i
        print(mapping)

nums = [2,7,11,15]
target = 18
mapp = twoSum(nums, target)
print(mapp)