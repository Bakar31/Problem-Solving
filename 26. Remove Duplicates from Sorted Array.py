"""
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

    """

nums = [0,0,1,1,1,2,2,3,3,4]
counter = 1
set_nums = set(nums)
print(len(set_nums))

for i in set_nums:
    count_value = nums.count(i)
    print(count_value)
    counter += (count_value - 1)
    print(counter)

print(list(set_nums))
print(counter)


j = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[j] = nums[i]
        j += 1
print(j)


